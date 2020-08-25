import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



SECRET_KEY = 'kr3u3@2s8$a_&3oy$q-$=1woj5vso!%q1(mm7%2(1itq#ig-16'

DEBUG = False

ALLOWED_HOSTS = ['45.10.110.71']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kondensat01@gmail.com'
EMAIL_HOST_PASSWORD = 'vladjous321123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAI_USE_SSL = False

DATABASES = {
	'default':{
		'ENGINE': 'django.db.backends.postgresql_psycop2',
		'NAME': 'piekdb',
		'USER': 'userdb',
		'PASSWORD': '123456',
		'HOST': 'localhost',
		'PORT': '5432',
 	}
}


STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')