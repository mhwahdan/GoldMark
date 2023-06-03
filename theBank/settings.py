from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.theBank.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4k-nez^xh@am=-8b7%fb&om9461u(op4m(6eh53(rr1-03e9s)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition
AUTH_USER_MODEL = 'users.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'PropertyMarket.apps.PropertyMarketConfig',
    'Blog.apps.BlogConfig',
    'ContactUs.apps.ContactusConfig',
    'FAQS.apps.FaqsConfig',
    'users.apps.UsersConfig',
    'flat_json_widget',
    'tinymce',
    'django.contrib.sites'
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

ROOT_URLCONF = 'theBank.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'theBank.wsgi.application'

# Database
# https://docs.theBank.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.theBank.com/en/3.2/ref/settings/#auth-password-validators

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]

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
    }
]


# Internationalization
# https://docs.theBank.com/en/3.2/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ACCOUNT_EMAIL_VERIFICATION = 'none'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.theBank.com/en/3.2/howto/static-files/

#STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static/'
]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.theBank.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TINYMCE_DEFAULT_CONFIG = {

    'height': 360,

    'width': 900,

    'cleanup_on_startup': True,

    'custom_undo_redo_levels': 20,

    'theme': 'silver',

    'plugins': '''

   textcolor save link image media preview codesample contextmenu

   table code lists fullscreen insertdatetime nonbreaking

   contextmenu directionality searchreplace wordcount visualblocks

   visualchars code fullscreen autolink lists charmap print hr

   anchor pagebreak

   ''',

    'toolbar1': '''

   fullscreen preview bold italic underline | fontselect,

   fontsizeselect | forecolor backcolor | alignleft alignright |

   aligncenter alignjustify | indent outdent | bullist numlist table |

   | link image media | codesample |



   ''',

    'toolbar2': '''

   visualblocks visualchars |

   charmap hr pagebreak nonbreaking anchor | code |

   ''',

    'contextmenu': 'formats | link image',

    'menubar': True,

    'statusbar': True,

}
