# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=^ff8pyv-!=dm4)^nn3r%q7yw4iy94j9^jdc0$wtc!ee2j9=au'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bdn',
        'USER': 'SomeOne',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
