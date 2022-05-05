# Librerias
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Rutas
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    #Database URL
    SQLALCHEMY_DATABASE_URI = 'sqlite:///Clientes.db'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
