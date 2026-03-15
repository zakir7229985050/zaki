import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-prod'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///teaching_platform.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'instance/uploads'
    MAX_CONTENT_LENGTH = 500 * 1024 * 1024  # 500MB max upload (videos)
    ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'pdf'}  # Video/PDF

    # UPI Payment
    PHONEPE_NUMBER = '7229985050'
    GOOGLEPAY_NUMBER = '7229985050'
    BANK_ACCOUNT = '30392342115'

    # Roles
    ROLES = {'Student': 1, 'Teacher': 2, 'Admin': 3}

