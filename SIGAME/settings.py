from pathlib import Path
import os, sys

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(1, os.path.join( os.path.dirname(__file__),  '../apps'))

SECRET_KEY = ''

DEBUG = False

ALLOWED_HOSTS = ['marquespy.pythonanywhere.com']

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',

  'GUIAS.apps.GuiasConfig',
  'CADASTRO.apps.CadastroConfig',
  'RESTRITO.apps.RestritoConfig',

  'crispy_forms',
  'crispy_bootstrap5',
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

ROOT_URLCONF = 'SIGAME.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [ os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'SIGAME.wsgi.application'


DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
  }
}

AUTH_PASSWORD_VALIDATORS = [
  # {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
  {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
  {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
  {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR / "static", ]

LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = "/accounts/login/"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
