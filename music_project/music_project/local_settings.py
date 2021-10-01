# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-alxg!*uy8_luepgx(=pc8n1&2l*&@+(_a+&zhkxs2ae896f5kl'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_project_database',
        'USER': 'root',
        'PASSWORD': 'j4bdfng34d',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
