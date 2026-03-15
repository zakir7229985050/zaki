from app import app, db
from models import User
from config import Config

with app.app_context():
    # Create default admin
    admin = User(username='admin', email='admin@edup latform.com', role='Admin')
    admin.set_password('admin123')
    db.session.add(admin)
    db.session.commit()
    print('Default admin created: username=admin, password=admin123, email=admin@eduplatform.com')

    # Create default student
    student = User(username='student', email='student@eduplatform.com', role='Student')
    student.set_password('student123')
    db.session.add(student)
    db.session.commit()
    print('Default student created: username=student, password=student123')

    # Create default teacher
    teacher = User(username='teacher', email='teacher@eduplatform.com', role='Teacher')
    teacher.set_password('teacher123')
    db.session.add(teacher)
    db.session.commit()
    print('Default teacher created: username=teacher, password=teacher123')

