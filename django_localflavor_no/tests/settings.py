# -*- coding: utf8 -*-

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_localflavor_no',
    }
}

INSTALLED_APPS = (
    'django_localflavor_no',
    'django_localflavor_no.tests',
)