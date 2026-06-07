/* ============================================
   HIREDIN — APP JAVASCRIPT
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {
    // Cookie Banner
    initCookieBanner();

    // Navbar scroll effect
    initNavbarScroll();

    // Builder functionality
    initBuilder();

    // Skills input
    initSkillsInput();

    // Smooth scroll for anchor links
    initSmoothScroll();
});

/* ============================================
   COOKIE BANNER
   ============================================ */
function initCookieBanner() {
    const banner = document.getElementById('cookie-banner');
    if (!banner) return;

    const accepted = localStorage.getItem('cookiesAccepted');
    const rejected = localStorage.getItem('cookiesRejected');

    if (!accepted && !rejected) {
        setTimeout(() => banner.classList.add('show'), 1000);
    }
}

function acceptCookies() {
    localStorage.setItem('cookiesAccepted', 'true');
    document.getElementById('cookie-banner').classList.remove('show');
}

function rejectCookies() {
    localStorage.setItem('cookiesRejected', 'true');
    document.getElementById('cookie-banner').classList.remove('show');
}

/* ============================================
   NAVBAR SCROLL
   ============================================ */
function initNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    if (!navbar) return;

    let lastScroll = 0;
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 50) {
            navbar.style.boxShadow = '0 4px 20px rgba(0,0,0,0.08)';
        } else {
            navbar.style.boxShadow = 'none';
        }

        lastScroll = currentScroll;
    }, { passive: true });
}

/* ============================================
   PASSWORD TOGGLE
   ============================================ */
function togglePassword(inputId, btn) {
    const input = document.getElementById(inputId);
    const icon = btn.querySelector('i');

    if (input.type === 'password') {
        input.type = 'text';
        icon.classList.remove('fa-eye');
        icon.classList.add('fa-eye-slash');
    } else {
        input.type = 'password';
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
    }
}

/* ============================================
   BUILDER FUNCTIONALITY
   ============================================ */
function initBuilder() {
    // Progress tracking
    updateProgress();

    // Auto-save on input
    const inputs = document.querySelectorAll('#resumeForm input, #resumeForm textarea, #resumeForm select');
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            updateProgress();
            updateLivePreview();
        });
    });
}

function updateProgress() {
    const inputs = document.querySelectorAll('#resumeForm input[required], #resumeForm textarea');
    let filled = 0;
    let total = 0;

    inputs.forEach(input => {
        if (input.value.trim()) filled++;
        total++;
    });

    const percent = Math.round((filled / total) * 100);
    const bar = document.getElementById('progressBar');
    const text = document.getElementById('progressText');

    if (bar) bar.style.width = percent + '%';
    if (text) text.textContent = percent + '% Complete';
}

function updateLivePreview() {
    const preview = document.getElementById('livePreview');
    if (!preview) return;

    const name = document.getElementById('fullName')?.value || 'Your Name';
    const title = document.getElementById('jobTitle')?.value || 'Professional Title';
    const email = document.getElementById('email')?.value || '';
    const phone = document.getElementById('phone')?.value || '';
    const location = document.getElementById('location')?.value || '';
    const summary = document.getElementById('summary')?.value || '';

    let html = '<div style="font-family: Inter, sans-serif; color: #0f172a;">';
    html += '<h2 style="font-size: 1.3rem; font-weight: 700; margin-bottom: 4px; color: #1e40af;">' + name + '</h2>';
    html += '<p style="font-size: 0.9rem; color: #64748b; margin-bottom: 8px;">' + title + '</p>';

    const contacts = [email, phone, location].filter(Boolean);
    if (contacts.length) {
        html += '<p style="font-size: 0.8rem; color: #94a3b8; margin-bottom: 16px;">' + contacts.join(' | ') + '</p>';
    }

    if (summary) {
        html += '<h4 style="font-size: 0.9rem; font-weight: 600; color: #1e40af; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 1px;">Professional Summary</h4>';
        html += '<p style="font-size: 0.85rem; color: #475569; line-height: 1.6;">' + summary + '</p>';
    }

    html += '</div>';
    preview.innerHTML = html;
}

/* ============================================
   ADD/REMOVE ITEMS
   ============================================ */
function addExperience() {
    const container = document.getElementById('experienceContainer');
    const item = document.createElement('div');
    item.className = 'experience-item';
    item.innerHTML = `
        <div class="row">
            <div class="col-md-6 mb-2">
                <input type="text" class="form-control" placeholder="Job Title" data-field="title">
            </div>
            <div class="col-md-6 mb-2">
                <input type="text" class="form-control" placeholder="Company Name" data-field="company">
            </div>
        </div>
        <div class="row">
            <div class="col-md-6 mb-2">
                <input type="text" class="form-control" placeholder="Duration" data-field="duration">
            </div>
            <div class="col-md-6 mb-2">
                <input type="text" class="form-control" placeholder="Location" data-field="location">
            </div>
        </div>
        <textarea class="form-control mb-2" rows="3" placeholder="Describe your responsibilities and achievements..." data-field="description"></textarea>
        <button type="button" class="btn btn-sm btn-outline-danger" onclick="removeItem(this)">
            <i class="fas fa-trash me-1"></i>Remove
        </button>
    `;
    container.appendChild(item);
    updateProgress();
}

function addEducation() {
    const container = document.getElementById('educationContainer');
    const item = document.createElement('div');
    item.className = 'education-item';
    item.innerHTML = `
        <div class="row">
            <div class="col-md-6 mb-2">
                <input type="text" class="form-control" placeholder="Degree/Certificate" data-field="degree">
            </div>
            <div class="col-md-6 mb-2">
                <input type="text" class="form-control" placeholder="Institution" data-field="institution">
            </div>
        </div>
        <div class="row">
            <div class="col-md-6 mb-2">
                <input type="text" class="form-control" placeholder="Year" data-field="year">
            </div>
            <div class="col-md-6 mb-2">
                <input type="text" class="form-control" placeholder="Grade/Percentage/CGPA" data-field="grade">
            </div>
        </div>
        <textarea class="form-control mb-2" rows="2" placeholder="Additional details..." data-field="details"></textarea>
        <button type="button" class="btn btn-sm btn-outline-danger" onclick="removeItem(this)">
            <i class="fas fa-trash me-1"></i>Remove
        </button>
    `;
    container.appendChild(item);
    updateProgress();
}

function addProject() {
    const container = document.getElementById('projectsContainer');
    const item = document.createElement('div');
    item.className = 'project-item';
    item.innerHTML = `
        <input type="text" class="form-control mb-2" placeholder="Project Name" data-field="name">
        <textarea class="form-control mb-2" rows="2" placeholder="Brief description..." data-field="description"></textarea>
        <input type="url" class="form-control mb-2" placeholder="Project URL (optional)" data-field="url">
        <button type="button" class="btn btn-sm btn-outline-danger" onclick="removeItem(this)">
            <i class="fas fa-trash me-1"></i>Remove
        </button>
    `;
    container.appendChild(item);
    updateProgress();
}

function addCertification() {
    const container = document.getElementById('certificationsContainer');
    const item = document.createElement('div');
    item.className = 'cert-item';
    item.innerHTML = `
        <input type="text" class="form-control mb-2" placeholder="Certification Name" data-field="name">
        <input type="text" class="form-control mb-2" placeholder="Issuing Organization" data-field="org">
        <input type="text" class="form-control mb-2" placeholder="Year" data-field="year">
        <button type="button" class="btn btn-sm btn-outline-danger" onclick="removeItem(this)">
            <i class="fas fa-trash me-1"></i>Remove
        </button>
    `;
    container.appendChild(item);
    updateProgress();
}

function addLanguage() {
    const container = document.getElementById('languagesContainer');
    const item = document.createElement('div');
    item.className = 'lang-item';
    item.innerHTML = `
        <div class="row">
            <div class="col-md-6 mb-2">
                <input type="text" class="form-control" placeholder="Language" data-field="name">
            </div>
            <div class="col-md-6 mb-2">
                <select class="form-select" data-field="level">
                    <option value="">Proficiency Level</option>
                    <option value="Native">Native</option>
                    <option value="Fluent">Fluent</option>
                    <option value="Advanced">Advanced</option>
                    <option value="Intermediate">Intermediate</option>
                    <option value="Basic">Basic</option>
                </select>
            </div>
        </div>
        <button type="button" class="btn btn-sm btn-outline-danger" onclick="removeItem(this)">
            <i class="fas fa-trash me-1"></i>Remove
        </button>
    `;
    container.appendChild(item);
    updateProgress();
}

function removeItem(btn) {
    btn.closest('.experience-item, .education-item, .project-item, .cert-item, .lang-item').remove();
    updateProgress();
}

/* ============================================
   SKILLS INPUT
   ============================================ */
function initSkillsInput() {
    const input = document.getElementById('skillsInput');
    const container = document.getElementById('skillsTags');
    if (!input || !container) return;

    input.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            const skill = this.value.trim();
            if (skill) {
                addSkillTag(skill, container);
                this.value = '';
                updateProgress();
            }
        }
    });

    input.addEventListener('blur', function() {
        const skill = this.value.trim();
        if (skill) {
            addSkillTag(skill, container);
            this.value = '';
            updateProgress();
        }
    });
}

function addSkillTag(skill, container) {
    const tag = document.createElement('span');
    tag.className = 'skill-tag';
    tag.innerHTML = skill + ' <span class="remove-skill" onclick="this.parentElement.remove(); updateProgress();">×</span>';
    container.appendChild(tag);
}

/* ============================================
   PHOTO UPLOAD
   ============================================ */
function handlePhotoUpload(input) {
    const preview = document.getElementById('photoPreview');
    if (!input.files || !input.files[0] || !preview) return;

    const file = input.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        preview.innerHTML = '<img src="' + e.target.result + '" style="max-width: 150px; max-height: 200px; border-radius: 8px; margin-bottom: 12px;"><p style="font-weight:600;">Photo uploaded</p>';

        // Upload to server
        const formData = new FormData();
        formData.append('photo', file);

        fetch('/api/upload-photo', {
            method: 'POST',
            body: formData
        })
        .then(r => r.json())
        .then(data => {
            if (data.success) {
                preview.dataset.path = data.path;
            }
        })
        .catch(err => console.error('Upload error:', err));
    };

    reader.readAsDataURL(file);
}

/* ============================================
   SAVE / DOWNLOAD
   ============================================ */
function saveResume() {
    const data = collectResumeData();

    fetch('/api/save-resume', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(r => r.json())
    .then(result => {
        if (result.success) {
            alert('Resume saved successfully!');
        } else {
            alert('Please login to save resumes.');
        }
    })
    .catch(err => {
        console.error('Save error:', err);
        alert('Please login to save resumes.');
    });
}

function downloadPDF() {
    const data = collectResumeData();

    fetch('/api/generate-pdf', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(r => r.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'hiredin_resume.pdf';
        document.body.appendChild(a);
        a.click();
        a.remove();
        window.URL.revokeObjectURL(url);
    })
    .catch(err => {
        console.error('PDF error:', err);
        alert('Error generating PDF. Please try again.');
    });
}

function downloadWord() {
    alert('Word export coming soon! Use PDF export for now.');
}

function collectResumeData() {
    const data = {
        name: document.getElementById('fullName')?.value || '',
        title: document.getElementById('jobTitle')?.value || '',
        email: document.getElementById('email')?.value || '',
        phone: document.getElementById('phone')?.value || '',
        location: document.getElementById('location')?.value || '',
        linkedin: document.getElementById('linkedin')?.value || '',
        summary: document.getElementById('summary')?.value || '',
        country: new URLSearchParams(window.location.search).get('country') || 'usa',
        photo_path: document.getElementById('photoPreview')?.dataset?.path || null
    };

    // Collect experience
    data.experience = [];
    document.querySelectorAll('.experience-item').forEach(item => {
        const exp = {};
        item.querySelectorAll('[data-field]').forEach(field => {
            exp[field.dataset.field] = field.value;
        });
        if (exp.title) data.experience.push(exp);
    });

    // Collect education
    data.education = [];
    document.querySelectorAll('.education-item').forEach(item => {
        const edu = {};
        item.querySelectorAll('[data-field]').forEach(field => {
            edu[field.dataset.field] = field.value;
        });
        if (edu.degree) data.education.push(edu);
    });

    // Collect skills
    data.skills = [];
    document.querySelectorAll('.skill-tag').forEach(tag => {
        const text = tag.textContent.replace('×', '').trim();
        if (text) data.skills.push(text);
    });

    // Collect projects
    data.projects = [];
    document.querySelectorAll('.project-item').forEach(item => {
        const proj = {};
        item.querySelectorAll('[data-field]').forEach(field => {
            proj[field.dataset.field] = field.value;
        });
        if (proj.name) data.projects.push(proj);
    });

    // Collect certifications
    data.certifications = [];
    document.querySelectorAll('.cert-item').forEach(item => {
        const cert = {};
        item.querySelectorAll('[data-field]').forEach(field => {
            cert[field.dataset.field] = field.value;
        });
        if (cert.name) data.certifications.push(cert.name);
    });

    // Collect languages
    data.languages = [];
    document.querySelectorAll('.lang-item').forEach(item => {
        const lang = {};
        item.querySelectorAll('[data-field]').forEach(field => {
            lang[field.dataset.field] = field.value;
        });
        if (lang.name) data.languages.push(lang);
    });

    return data;
}

/* ============================================
   ATS CHECKER
   ============================================ */
function analyzeATS() {
    const text = document.getElementById('resumeText')?.value || '';
    const jobTitle = document.getElementById('jobTitleInput')?.value || '';
    const resultDiv = document.getElementById('atsResult');

    if (!text.trim()) {
        alert('Please paste your resume text first.');
        return;
    }

    resultDiv.classList.remove('d-none');
    document.getElementById('scoreValue').textContent = '...';
    document.getElementById('scoreTitle').textContent = 'Analyzing...';

    fetch('/api/analyze-ats', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text, job_title: jobTitle })
    })
    .then(r => r.json())
    .then(data => {
        document.getElementById('scoreValue').textContent = data.score;
        document.getElementById('scoreTitle').textContent = getScoreTitle(data.score);
        document.getElementById('scoreDesc').textContent = 'Based on ' + data.word_count + ' words analyzed';

        // Update score circle color
        const circle = document.getElementById('scoreCircle');
        circle.style.background = getScoreGradient(data.score);

        // Feedback
        const feedbackList = document.getElementById('feedbackList');
        feedbackList.innerHTML = '';
        if (data.feedback && data.feedback.length) {
            data.feedback.forEach(item => {
                feedbackList.innerHTML += '<div class="alert alert-warning mb-2"><i class="fas fa-exclamation-circle me-2"></i>' + item + '</div>';
            });
        } else {
            feedbackList.innerHTML = '<div class="alert alert-success"><i class="fas fa-check-circle me-2"></i>Great job! No major issues found.</div>';
        }

        // Keywords
        const keywordsList = document.getElementById('keywordsList');
        keywordsList.innerHTML = '';
        if (data.found_keywords && data.found_keywords.length) {
            data.found_keywords.forEach(kw => {
                keywordsList.innerHTML += '<span class="badge bg-success me-2 mb-2">' + kw + '</span>';
            });
        } else {
            keywordsList.innerHTML = '<p class="text-muted">No matching keywords found. Try adding relevant industry terms.</p>';
        }
    })
    .catch(err => {
        console.error('ATS error:', err);
        alert('Error analyzing resume. Please try again.');
    });
}

function getScoreTitle(score) {
    if (score >= 80) return 'Excellent! Your resume is ATS-friendly.';
    if (score >= 60) return 'Good, but there is room for improvement.';
    if (score >= 40) return 'Fair. Several issues need fixing.';
    return 'Poor. Major improvements needed.';
}

function getScoreGradient(score) {
    if (score >= 80) return 'linear-gradient(135deg, #10b981, #059669)';
    if (score >= 60) return 'linear-gradient(135deg, #f59e0b, #d97706)';
    if (score >= 40) return 'linear-gradient(135deg, #f97316, #ea580c)';
    return 'linear-gradient(135deg, #ef4444, #dc2626)';
}

/* ============================================
   REJECTION PREDICTOR
   ============================================ */
function analyzeRejection() {
    const text = document.getElementById('rejectionText')?.value || '';
    const resultDiv = document.getElementById('rejectionResult');

    if (!text.trim()) {
        alert('Please paste your resume text first.');
        return;
    }

    resultDiv.classList.remove('d-none');
    document.getElementById('riskScore').textContent = '...';
    document.getElementById('riskLevel').textContent = 'Analyzing...';

    fetch('/api/rejection-risk', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
    })
    .then(r => r.json())
    .then(data => {
        document.getElementById('riskScore').textContent = data.score;
        document.getElementById('riskLevel').textContent = data.risk_level + ' Risk — ' + (data.score >= 80 ? 'Your resume looks strong!' : 'Fix the issues below to improve your chances.');
        document.getElementById('riskDesc').textContent = 'Analysis complete. Review the risk factors below.';

        const card = document.getElementById('riskCard');
        if (data.color === 'green') {
            card.querySelector('.risk-score').style.background = 'linear-gradient(135deg, #10b981, #059669)';
        } else if (data.color === 'orange') {
            card.querySelector('.risk-score').style.background = 'linear-gradient(135deg, #f59e0b, #d97706)';
        } else {
            card.querySelector('.risk-score').style.background = 'linear-gradient(135deg, #ef4444, #dc2626)';
        }

        const risksList = document.getElementById('risksList');
        risksList.innerHTML = '';
        if (data.risks && data.risks.length) {
            data.risks.forEach(risk => {
                const severityClass = risk.severity === 'high' ? 'alert-danger' : (risk.severity === 'medium' ? 'alert-warning' : 'alert-info');
                const icon = risk.severity === 'high' ? 'fa-times-circle' : (risk.severity === 'medium' ? 'fa-exclamation-circle' : 'fa-info-circle');
                risksList.innerHTML += '<div class="alert ' + severityClass + ' mb-2"><i class="fas ' + icon + ' me-2"></i><strong>' + risk.severity.toUpperCase() + ':</strong> ' + risk.message + '</div>';
            });
        } else {
            risksList.innerHTML = '<div class="alert alert-success"><i class="fas fa-check-circle me-2"></i>No major risk factors found! Your resume looks good.</div>';
        }
    })
    .catch(err => {
        console.error('Rejection error:', err);
        alert('Error analyzing resume. Please try again.');
    });
}

/* ============================================
   MIGRATION
   ============================================ */
function getMigrationSteps() {
    const from = document.getElementById('fromCountry')?.value || 'usa';
    const to = document.getElementById('toCountry')?.value || 'uk';
    const resultDiv = document.getElementById('migrationResult');

    resultDiv.classList.remove('d-none');
    document.getElementById('migrationSteps').innerHTML = '<div class="text-center"><i class="fas fa-spinner fa-spin"></i> Loading...</div>';

    fetch('/api/migration-steps', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ from: from, to: to })
    })
    .then(r => r.json())
    .then(data => {
        let html = '<ol class="list-group list-group-numbered">';
        data.steps.forEach(step => {
            html += '<li class="list-group-item d-flex justify-content-between align-items-start">';
            html += '<div class="ms-2 me-auto">' + step + '</div>';
            html += '<i class="fas fa-check-circle text-success"></i>';
            html += '</li>';
        });
        html += '</ol>';
        document.getElementById('migrationSteps').innerHTML = html;
    })
    .catch(err => {
        console.error('Migration error:', err);
        document.getElementById('migrationSteps').innerHTML = '<div class="alert alert-danger">Error loading migration steps.</div>';
    });
}

/* ============================================
   MULTI-CONVERT
   ============================================ */
function convertMulti() {
    const checked = document.querySelectorAll('.country-check input:checked');
    const countries = Array.from(checked).map(c => c.value);

    if (countries.length === 0) {
        alert('Please select at least one country.');
        return;
    }

    alert('Generating resumes for: ' + countries.join(', ') + '...\n(Feature coming soon - will generate PDFs for each selected country)');
}

/* ============================================
   JOB LINK IMAGE PREVIEW
   ============================================ */
function previewImage(input) {
    const placeholder = document.getElementById('uploadPlaceholder');
    const preview = document.getElementById('imagePreview');
    const img = document.getElementById('previewImg');

    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
            img.src = e.target.result;
            placeholder.classList.add('d-none');
            preview.classList.remove('d-none');
        };
        reader.readAsDataURL(input.files[0]);
    }
}

function removeImage() {
    const input = document.getElementById('jobImage');
    const placeholder = document.getElementById('uploadPlaceholder');
    const preview = document.getElementById('imagePreview');

    input.value = '';
    placeholder.classList.remove('d-none');
    preview.classList.add('d-none');
}

/* ============================================
   FAQ TOGGLE
   ============================================ */
function toggleFaq(element) {
    const answer = element.nextElementSibling;
    const isActive = element.classList.contains('active');

    // Close all
    document.querySelectorAll('.faq-question').forEach(q => q.classList.remove('active'));
    document.querySelectorAll('.faq-answer').forEach(a => a.classList.remove('show'));

    // Open clicked if not already active
    if (!isActive) {
        element.classList.add('active');
        answer.classList.add('show');
    }
}

/* ============================================
   SMOOTH SCROLL
   ============================================ */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
}

/* ============================================
   GENERATE SUMMARY (AI)
   ============================================ */
function generateSummary() {
    const title = document.getElementById('jobTitle')?.value || 'professional';
    const summaries = [
        'Results-driven ' + title + ' with 5+ years of experience delivering high-impact solutions. Proven track record of leading cross-functional teams and driving measurable business outcomes.',
        'Dynamic ' + title + ' skilled in strategic planning, execution, and stakeholder management. Passionate about leveraging data-driven insights to optimize performance and achieve organizational goals.',
        'Experienced ' + title + ' with expertise in modern methodologies and best practices. Committed to continuous improvement and delivering exceptional results in fast-paced environments.'
    ];
    const summary = document.getElementById('summary');
    if (summary) {
        summary.value = summaries[Math.floor(Math.random() * summaries.length)];
        updateProgress();
        updateLivePreview();
    }
}

/* ============================================
   RUN ATS CHECK FROM BUILDER
   ============================================ */
function runATSCheck() {
    const summary = document.getElementById('summary')?.value || '';
    const text = collectResumeText();

    if (!text.trim()) {
        alert('Please fill in some resume details first.');
        return;
    }

    window.open('/analysis', '_blank');
}

function collectResumeText() {
    let text = '';
    document.querySelectorAll('#resumeForm input, #resumeForm textarea').forEach(input => {
        if (input.value) text += input.value + ' ';
    });
    return text;
}
