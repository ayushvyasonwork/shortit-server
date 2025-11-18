from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'dev-secret'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'django.contrib.sessions',
    'shortener',
    'corsheaders',
]
MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
]
ROOT_URLCONF = 'shortit.urls'
TEMPLATES = []
WSGI_APPLICATION = 'shortit.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
CORS_ALLOW_HEADERS = [
    '*',
]

CORS_ALLOW_METHODS = [
    '*',
]
CORS_ALLOW_PRIVATE_NETWORK = True
CORS_ALLOW_ALL_ORIGINS = True


STATIC_URL = '/static/'
