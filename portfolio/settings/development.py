SECRET_KEY = 'zg48b3!rgx1wb-v75fc5d-#y&2b65hll5n&+^xe@1u7c2vpbls'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'portfoliodb',
        'USER': 'root',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}