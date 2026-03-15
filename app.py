from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from config import Config
from models import db, User, Course, Enrollment, Lecture, Note, PaymentLog
import os

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# DB Create
with app.app_context():
    db.create_all()

# Allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Home
@app.route('/')
def home():
    return render_template('home.html')

# Placeholder routes for all pages
@app.route('/login', methods=['GET', 'POST'])
def login():
    # TODO: Implement
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # TODO: Implement
    return render_template('register.html')

@app.route('/student_dashboard')
@login_required
def student_dashboard():
    if current_user.role != 'Student':
        flash('Access denied')
        return redirect(url_for('home'))
    return render_template('student_dashboard.html')

# More routes to be added...
@app.route('/upload_video', methods=['POST'])
@login_required
def upload_video():
    if 'file' not in request.files:
        flash('No file')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'videos'), exist_ok=True)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'videos', filename))
        # Save to DB
        lecture = Lecture(title=file.filename, video_path=f'videos/{filename}', course_id=request.form.get('course_id'))
        db.session.add(lecture)
        db.session.commit()
        flash('Uploaded')
    return redirect(url_for('student_dashboard'))

# Serve uploads
@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True, port=5000)

