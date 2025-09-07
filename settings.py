SECRET_KEY = 'dummy-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'listings',
]

ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'alx_travel_app.wsgi.application'
