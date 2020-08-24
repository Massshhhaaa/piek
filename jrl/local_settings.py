import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'kr3u3@2s8$a_&5oy$q-$=1woj3vsi!%q1(mm7%2(1itq#ig-16'

DEBUG =  True

ALLOWED_HOSTS = ['45.10.110.71','localhost']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kondensat01@gmail.com'
EMAIL_HOST_PASSWORD = 'vladjous321123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAI_USE_SSL = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
