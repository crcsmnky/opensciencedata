import json
import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

try:
    envfile = open('/home/dotcloud/environment.json')
    env = json.load(envfile)
    dbengn = 'django.db.backends.postgresql_psycopg2'
    dbname = 'template1'
    dbuser = env['DOTCLOUD_DB_SQL_LOGIN']
    dbpass = env['DOTCLOUD_DB_SQL_PASSWORD']
    dbhost = env['DOTCLOUD_DB_SQL_HOST']
    dbport = env['DOTCLOUD_DB_SQL_PORT']
except IOError:
    dbengn = 'django.db.backends.sqlite3'
    dbname = 'opensciencedata.sq3'
    dbuser = ''
    dbpass = ''
    dbhost = ''
    dbport = 0

DATABASES = {
    'default': {
        'ENGINE': dbengn,
        'NAME': dbname,
        'USER': dbuser,
        'PASSWORD': dbpass,
        'HOST': dbhost,
        'PORT': dbport,
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'uploads')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://localhost:8000/uploads/'

STATIC_URL = 'http://localhost:8000/static/'

LOGIN_URL = '/account/login'

LOGIN_REDIRECT_URL = '/comp/'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
    os.path.join(os.path.dirname(__file__), 'templates', 'datasets'),
    os.path.join(os.path.dirname(__file__), 'templates', 'users'),
    os.path.join(os.path.dirname(__file__), 'templates', 'tags'),
)
