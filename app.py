
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session, send_file, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
import random
import datetime
import json
from io import BytesIO

from utils.country_engine import get_country_format, get_all_countries
from utils.ats_engine import analyze_ats_score
from utils.mistake_detector import detect_mistakes
from utils.coach_engine import get_country_coach
from utils.migration_engine import get_migration_steps
from utils.predictor_engine import analyze_rejection_risk
from utils.pdf_engine import generate_pdf

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'hiredin-secret-key-2024-secure')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///hiredin.db').replace('postgres://', 'postgresql://')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'doc', 'docx'}

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# ==================== DATABASE MODELS ====================

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(50), default='usa')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    is_verified = db.Column(db.Boolean, default=True)
    resumes = db.relationship('Resume', backref='user', lazy=True)
    messages = db.relationship('ContactMessage', backref='user', lazy=True)

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    country_code = db.Column(db.String(20), nullable=False)
    data = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    ats_score = db.Column(db.Integer, default=0)
    photo_path = db.Column(db.String(300), nullable=True)

class JobLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    job_url = db.Column(db.String(500), nullable=True)
    job_title = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    role_type = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    image_path = db.Column(db.String(300), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='unread')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ==================== HELPER FUNCTIONS ====================

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ==================== ROUTES ====================

@app.route('/')
def index():
    countries = get_all_countries()
    return render_template('index.html', countries=countries)

@app.route('/builder')
def builder():
    country = request.args.get('country', 'usa')
    country_data = get_country_format(country)
    countries = get_all_countries()
    return render_template('builder.html', country=country, country_data=country_data, countries=countries)

@app.route('/preview')
def preview():
    return render_template('preview.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/coach')
def coach():
    country = request.args.get('country', 'usa')
    coach_data = get_country_coach(country)
    return render_template('coach.html', coach_data=coach_data, country=country)

@app.route('/migration')
def migration():
    return render_template('migration.html')

@app.route('/multi-convert')
def multi_convert():
    return render_template('multi_convert.html')

@app.route('/rejection-predictor')
def rejection_predictor():
    return render_template('rejection_predictor.html')

@app.route('/job-link', methods=['GET', 'POST'])
def job_link():
    if request.method == 'POST':
        job_url = request.form.get('job_url', '')
        job_title = request.form.get('job_title', '')
        company = request.form.get('company', '')
        country = request.form.get('country', '')
        role_type = request.form.get('role_type', '')
        description = request.form.get('description', '')

        image_path = None
        if 'job_image' in request.files:
            file = request.files['job_image']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(image_path)
                image_path = image_path.replace('static/', '')

        job = JobLink(
            user_id=current_user.id if current_user.is_authenticated else None,
            job_url=job_url,
            job_title=job_title,
            company=company,
            country=country,
            role_type=role_type,
            description=description,
            image_path=image_path
        )
        db.session.add(job)
        db.session.commit()

        flash('Job details saved! Now build your resume tailored for this job.', 'success')
        return redirect(url_for('builder', country=country.lower() if country else 'usa'))

    jobs = JobLink.query.order_by(JobLink.created_at.desc()).limit(10).all()
    return render_template('job_link.html', jobs=jobs)

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/cookies')
def cookies():
    return render_template('cookies.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/help')
def help_page():
    return render_template('help.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()

        if not name or not email or not subject or not message:
            flash('Please fill in all fields.', 'danger')
            return redirect(url_for('contact'))

        msg = ContactMessage(
            user_id=current_user.id if current_user.is_authenticated else None,
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        db.session.add(msg)
        db.session.commit()

        flash('Message sent successfully! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/security')
def security():
    return render_template('security.html')

# ==================== AUTH ROUTES ====================

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_input = request.form.get('login_input', '').strip()
        password = request.form.get('password', '')

        user = User.query.filter(
            db.or_(
                User.email == login_input,
                User.username == login_input
            )
        ).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Welcome back to HiredIn!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        country = request.form.get('country', 'usa')

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('register'))

        if len(password) < 6:
            flash('Password must be at least 6 characters.', 'danger')
            return redirect(url_for('register'))

        if User.query.filter_by(username=username).first():
            flash('Username already taken.', 'danger')
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'danger')
            return redirect(url_for('register'))

        user = User(
            name=name,
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            country=country,
            is_verified=True
        )
        db.session.add(user)
        db.session.commit()

        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))

    countries = get_all_countries()
    return render_template('register.html', countries=countries)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    resumes = Resume.query.filter_by(user_id=current_user.id).order_by(Resume.created_at.desc()).all()
    jobs = JobLink.query.filter_by(user_id=current_user.id).order_by(JobLink.created_at.desc()).all()
    return render_template('dashboard.html', resumes=resumes, jobs=jobs)

@app.route('/profile')
@login_required
def profile():
    countries = get_all_countries()
    return render_template('profile.html', countries=countries)

@app.route('/update-profile', methods=['POST'])
@login_required
def update_profile():
    current_user.name = request.form.get('name', current_user.name)
    current_user.email = request.form.get('email', current_user.email)
    current_user.country = request.form.get('country', current_user.country)
    db.session.commit()
    flash('Profile updated successfully!', 'success')
    return redirect(url_for('profile'))

# ==================== ADMIN / MESSAGES ====================

@app.route('/admin/messages')
@login_required
def admin_messages():
    messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
    return render_template('admin_messages.html', messages=messages)

@app.route('/admin/message/<int:msg_id>/reply', methods=['POST'])
@login_required
def reply_message(msg_id):
    msg = ContactMessage.query.get_or_404(msg_id)
    msg.status = 'replied'
    db.session.commit()
    flash('Message marked as replied.', 'success')
    return redirect(url_for('admin_messages'))

@app.route('/admin/message/<int:msg_id>/read')
@login_required
def read_message(msg_id):
    msg = ContactMessage.query.get_or_404(msg_id)
    msg.status = 'read'
    db.session.commit()
    return redirect(url_for('admin_messages'))

# ==================== API ROUTES ====================

@app.route('/api/analyze-ats', methods=['POST'])
def api_analyze_ats():
    data = request.json
    resume_text = data.get('text', '')
    job_title = data.get('job_title', '')
    result = analyze_ats_score(resume_text, job_title)
    return jsonify(result)

@app.route('/api/detect-mistakes', methods=['POST'])
def api_detect_mistakes():
    data = request.json
    resume_text = data.get('text', '')
    mistakes = detect_mistakes(resume_text)
    return jsonify({"mistakes": mistakes})

@app.route('/api/rejection-risk', methods=['POST'])
def api_rejection_risk():
    data = request.json
    resume_text = data.get('text', '')
    result = analyze_rejection_risk(resume_text)
    return jsonify(result)

@app.route('/api/migration-steps', methods=['POST'])
def api_migration_steps():
    data = request.json
    from_country = data.get('from', 'usa')
    to_country = data.get('to', 'uk')
    steps = get_migration_steps(from_country, to_country)
    return jsonify({"steps": steps})

@app.route('/api/save-resume', methods=['POST'])
@login_required
def api_save_resume():
    data = request.json
    resume = Resume(
        user_id=current_user.id,
        title=data.get('title', 'Untitled Resume'),
        country_code=data.get('country', 'usa'),
        data=json.dumps(data),
        ats_score=data.get('ats_score', 0)
    )
    db.session.add(resume)
    db.session.commit()
    return jsonify({"success": True, "id": resume.id})

@app.route('/api/generate-pdf', methods=['POST'])
def api_generate_pdf():
    data = request.json
    country = data.get('country', 'usa')
    photo_path = data.get('photo_path')
    if photo_path:
        photo_path = os.path.join('static', photo_path)

    pdf = generate_pdf(data, country, photo_path)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=hiredin_resume.pdf'
    return response

@app.route('/api/upload-photo', methods=['POST'])
def api_upload_photo():
    if 'photo' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['photo']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({"success": True, "path": filepath.replace('static/', '')})

    return jsonify({"error": "Invalid file type"}), 400

# ==================== INITIALIZE ====================

with app.app_context():
    db.create_all()
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
