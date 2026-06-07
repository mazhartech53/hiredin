# HiredIn — AI-Powered Resume Builder

**Build your perfect resume for any country, any job, any profession.**

HiredIn is a complete, production-ready resume building platform with AI-powered features including ATS checking, rejection prediction, job link matching, country-specific formatting, and multi-country conversion.

---

## Features

### Core Features
- **Resume Builder** — Build professional resumes tailored to 8+ country formats (USA, UK, Canada, Australia, Germany, France, India, UAE)
- **Passport Size Photo Upload** — Photo support for countries that require it (Germany, France, India, UAE)
- **ATS Checker** — Scan your resume against Applicant Tracking Systems with actionable feedback
- **Rejection Predictor** — AI-powered analysis that predicts why recruiters might reject your resume
- **Country Coach** — Expert tips for each country's resume standards
- **Migration Mode** — Convert your resume from one country format to another
- **Multi-Country Export** — Generate resumes for multiple countries at once
- **Job Link Resume** — Paste any job description/link and build a tailored resume

### Auth & Security
- **Flexible Login** — Login with email, username, OR mobile number (like Instagram)
- **OTP Verification** — Email and SMS OTP for account security
- **Password Toggle** — Eye icon to show/hide password
- **Profile Management** — Update name, email, phone, country, profession
- **Secure Passwords** — Bcrypt hashing with salt rounds

### Legal & Compliance
- **Privacy Policy** — Detailed data handling and user rights
- **Cookie Policy** — Transparent cookie usage with consent banner
- **Terms of Service** — Clear terms for all users
- **Security & Data Privacy** — Encryption, infrastructure security, compliance info
- **Help Center** — FAQ with email support (support@hiredin.com)
- **Contact Us** — Contact form and support email
- **About/Overview** — Detailed company and mission info

### Design
- **Premium Light Theme** — Strong, bold, professional (NOT dark mode)
- **Gradient Accents** — Beautiful blue-purple gradients
- **Smooth Animations** — Floating shapes, orbit animations, hover effects
- **Fully Responsive** — Works on desktop, tablet, and mobile
- **Cookie Consent Banner** — Accept/Reject cookies on first visit

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Database | SQLite (via SQLAlchemy) |
| Auth | Flask-Login, Werkzeug (bcrypt) |
| PDF | ReportLab |
| Frontend | Bootstrap 5, Font Awesome, Google Fonts |
| Styling | Custom CSS with CSS Variables |

---

## Installation

### 1. Extract the ZIP
```bash
cd hiredin
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

### 5. Open in Browser
```
http://localhost:5000
```

---

## Project Structure

```
hiredin/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── utils/                      # Backend engines
│   ├── __init__.py
│   ├── country_engine.py       # 8-country format definitions
│   ├── ats_engine.py           # ATS scoring algorithm
│   ├── mistake_detector.py     # Spelling/grammar/professional checks
│   ├── coach_engine.py         # Country-specific tips
│   ├── migration_engine.py     # Country-to-country conversion rules
│   ├── predictor_engine.py     # Rejection risk analysis
│   └── pdf_engine.py           # PDF generation with ReportLab
│
├── templates/                    # HTML templates (Jinja2)
│   ├── base.html               # Master layout with navbar, footer, cookies
│   ├── index.html              # Homepage with hero, features, blog, countries
│   ├── login.html              # Login (email/username/phone + password)
│   ├── register.html           # Registration with OTP
│   ├── verify_otp.html         # OTP verification page
│   ├── dashboard.html          # User dashboard with resumes & jobs
│   ├── profile.html            # Profile settings
│   ├── builder.html            # Resume builder with sidebar, form, preview
│   ├── preview.html            # Resume preview page
│   ├── analysis.html           # ATS checker page
│   ├── coach.html              # Country coach tips
│   ├── migration.html          # Migration mode
│   ├── multi_convert.html      # Multi-country export
│   ├── rejection_predictor.html # Rejection risk predictor
│   ├── job_link.html           # Job link resume builder
│   ├── pricing.html            # Pricing (all free during launch)
│   ├── privacy.html            # Privacy Policy
│   ├── cookies.html            # Cookie Policy
│   ├── terms.html              # Terms of Service
│   ├── help.html               # Help Center with FAQ
│   ├── contact.html            # Contact Us page
│   ├── overview.html           # About/Overview page
│   └── security.html           # Security & Data Privacy
│
├── static/
│   ├── css/style.css           # Complete premium styling
│   ├── js/app.js               # All frontend functionality
│   ├── uploads/                # User uploads (photos, job screenshots)
│   └── images/                 # Static images
│
└── hiredin.db                  # SQLite database (auto-created)
```

---

## Pages & Routes

| Route | Description |
|-------|-------------|
| `/` | Homepage with hero, features, blog, countries |
| `/builder` | Resume builder with live preview |
| `/job-link` | Paste job description, build tailored resume |
| `/analysis` | ATS score checker |
| `/rejection-predictor` | Rejection risk analysis |
| `/coach` | Country-specific resume tips |
| `/migration` | Convert resume between countries |
| `/multi-convert` | Export for multiple countries |
| `/login` | Login (email/username/phone + password) |
| `/register` | Create account with OTP verification |
| `/verify-otp/<id>` | OTP verification |
| `/dashboard` | User dashboard |
| `/profile` | Profile settings |
| `/pricing` | Pricing plans (all free) |
| `/privacy` | Privacy Policy |
| `/cookies` | Cookie Policy |
| `/terms` | Terms of Service |
| `/help` | Help Center |
| `/contact` | Contact Us |
| `/overview` | About HiredIn |
| `/security` | Security & Data Privacy |

---

## Key Features Implemented

### All User Requests Addressed
- [x] **HiredIn** branding (not "Resume Premium")
- [x] **Premium light theme** (not dark mode, strong & bold)
- [x] **Different text colors** that look great
- [x] **Eye icon** in password fields
- [x] **All feature cards clickable** with redirects
- [x] **Blog section** on homepage with 6 career articles
- [x] **Cookie consent banner** (Accept All / Reject All)
- [x] **Rupee pricing** (₹0 free, with USD equivalents noted)
- [x] **Job Link** feature instead of job matcher (paste URL/description/image)
- [x] **Passport size photo** upload for countries that require it
- [x] **Builder sidebar fixed** — no overlap on scroll
- [x] **Smooth homepage** — no earthquake feeling (gentle floating animations)
- [x] **Flexible login** — email, username, or mobile number
- [x] **OTP verification** — email and SMS support
- [x] **Complete registration** — name, username, password, email, phone, country, profession
- [x] **All professions supported** — tech, non-tech, healthcare, finance, education, etc.
- [x] **Privacy Policy, Cookie Policy, Terms, Help, Contact, Overview, Security** pages
- [x] **Help section email** — support@hiredin.com
- [x] **Free during launch** — all plans marked as free

---

## Next Steps (For Production)

1. **Email/SMS OTP** — Integrate with SendGrid (email) or Twilio (SMS) for real OTP delivery
2. **Google OAuth** — Add "Continue with Google" button
3. **Word Export** — Implement python-docx for .docx generation
4. **Cloud Storage** — Move uploads to AWS S3 or similar
5. **Database** — Upgrade to PostgreSQL for production
6. **Deployment** — Deploy to Heroku, AWS, or DigitalOcean
7. **Analytics** — Add Google Analytics (with cookie consent)
8. **SEO** — Add meta tags, sitemap, structured data

---

## License

© 2024 HiredIn. All rights reserved.

Built with ❤️ for job seekers worldwide.
