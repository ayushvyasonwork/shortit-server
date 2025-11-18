import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# SECURITY & ENV SETTINGS
# -------------------------

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")

# DEBUG = True for local, False on Render
DEBUG = os.getenv("DEBUG", "True") == "True"

# Allowed hosts (production + local)
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com",
    "shortit.projects.ayushvyas.me",
]

# -------------------------
# INSTALLED APPS
# -------------------------

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.auth",
    "django.contrib.sessions",
    "shortener",
    "corsheaders",
]

# -------------------------
# MIDDLEWARE
# -------------------------

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",   # MUST BE FIRST
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "shortit.urls"
TEMPLATES = []
WSGI_APPLICATION = "shortit.wsgi.application"

# -------------------------
# DATABASE
# -------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# -------------------------
# CORS CONFIG (works for Chrome extension)
# -------------------------

CORS_ALLOW_ALL_ORIGINS = True   # OK for dev & extension usage
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_PRIVATE_NETWORK = True

CORS_ALLOW_HEADERS = ["*"]
CORS_ALLOW_METHODS = ["*"]

# -------------------------
# STATIC FILES (Render needs this)
# -------------------------

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# -------------------------
# CUSTOM SHORT HOST
# -------------------------

SHORT_HOST = os.getenv("SHORT_HOST", "localhost:8000")
