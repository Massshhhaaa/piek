import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'kr3u3@2s8$a_&5oy$q-$=1woj3vsi!%q1(mm7%2(1itq#ig-16'

DEBUG =  True

ALLOWED_HOSTS = ['45.10.110.71','localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = '/media/'
