
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SESSION_COOKIE_AGE = 43200

ALLOWED_HOSTS = ['45.10.110.71', 'localhost', '127.0.0.1', '45.10.110.58','piek.ru']

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'pr@piek.ru'
EMAIL_HOST_PASSWORD = 'oevvvmohbdmddyru'
DEFAULT_FROM_EMAIL = 'pr@piek.ru'
EMAIL_USE_TLS = True

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False
COMPRESS_OUTPUT_DIR = 'cache'

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'compressor',
    'mainapp',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jrl.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'jrl.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)



# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

COMPRESS_ROOT = 'static/'
STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")






JAZZMIN_SETTINGS = {
    # title of the window
    'site_title': 'Piek Admin',

    # Title on the brand, and the login screen (19 chars max)
    'site_header': 'Piek',


    # Welcome text on the login screen
    'welcome_sign': 'Welcome to piek',

    # The model admin to search from the search bar, search bar omitted if excluded

    # Field name on user model that contains avatar image
    'user_avatar': None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    'topmenu_links': [

        # Url that gets reversed (Permissions can be added)
        {'name': 'Home',  'url': 'admin:index', 'permissions': ['auth.view_user']},
        {'name': 'Piek',  'url': 'http://piek.ru'},

    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    'usermenu_links': [
        {'model': 'auth.user'}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    'show_sidebar': False,

    # Whether to aut expand the menu
    'navigation_expanded': True,

    # Hide these apps when generating side menu e.g (auth)
    'hide_apps': [],

    # Hide these models when generating side menu (e.g auth.user)
    'hide_models': [],

    # List of apps to base side menu ordering off of (does not need to contain all apps)
    'order_with_respect_to': ['accounts', 'polls'],

    # Custom links to append to app groups, keyed on app name
    'custom_links': {
        'polls': [{
            'name': 'Make Messages',
            'url': 'make_messages',
            'icon': 'fa-comments',
            'permissions': ['polls.view_poll']
        }]
    },

    # Custom icons for side menu apps/models See https://www.fontawesomecheatsheet.com/font-awesome-cheatsheet-5x/
    # for a list of icon classes
    'icons': {
        'auth': 'fa-users-cog',
        'auth.user': 'fa-user',
        'auth.Group': 'fa-users',
    },
    # Icons that are used when one is not manually specified
    'default_icon_parents': 'fa-chevron-circle-right',
    'default_icon_children': 'fa-circle',

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": '../static/admin/admin.css',
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs",},
}

TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor paste save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen bold italic underline | styleselect | fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | paste pastetext |
            ''',
    'toolbar2': '''
              code |visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'content_css' : '/static/css/SubgroupDetailView.css',
    'statusbar': True,
    'min_height': '300',
}



try:
    from .local_settings import *
except ImportError:
    from .prod_settings import *
