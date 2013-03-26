import os
basedir = os.path.abspath(os.path.dirname(__file__))



class Config(object):
    STATIC = os.path.join(basedir, 'psc_app/static')
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    POSTS_PER_PAGE = 5
    CSRF_ENABLED = True
    SECRET_KEY = '\x8d@\xfb\x8f#Sm\x0bS\x1b\xef\xdd\xf3\x0bt\xf4fl 8\x9b\x14\x88\xa4'
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db/db_repository')
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    ADMINS = ['solidparallel6890@gmail.com']
    
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/psc_app.db')

    
class ProductionConfig():
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://takosuke:tiger@localhost/mydatabase'
    


