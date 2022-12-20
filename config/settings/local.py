from .base import *
from .base import env

DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-wd8hm9@cf=whz-sbka^i@ozuz_sug#d07pq8_=(z^zzu37%3s2",
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]


