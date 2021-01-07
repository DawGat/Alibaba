import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kl385Lod#n8*akWM#23neR831'
