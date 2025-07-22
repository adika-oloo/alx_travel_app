
# settings.py snippet

# Swagger config
INSTALLED_APPS = [
    ...
    'drf_yasg',
    'rest_framework',
    'listings',  # your app
]

# MySQL config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db',
        'USER': 'your_user',
        'PASSWORD': 'your_pass',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
