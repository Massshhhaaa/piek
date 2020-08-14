import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



SECRET_KEY = 'kr3u3@2s8$a_&3oy$q-$=1woj5vso!%q1(mm7%2(1itq#ig-16'

DEBUG = False

ALLOWED_HOSTS = ['45.10.110.71']


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


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')