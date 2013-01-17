import os
basedir = os.path.abspath(os.path.dirname(__file__))

#STATIC = os.path.join('/Users/mariocampos/Documents/_PROJECTS/PizzaSuicideClub/pizzasuicideclub/psc_app/static')
STATIC = os.path.join(basedir, 'psc_app/static')
UPLOAD_FOLDER = os.path.join(basedir, 'psc_app/static/uploads')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/psc_app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db/db_repository')
POSTS_PER_PAGE = 5

CSRF_ENABLED = True
SECRET_KEY = '\x8d@\xfb\x8f#Sm\x0bS\x1b\xef\xdd\xf3\x0bt\xf4fl 8\x9b\x14\x88\xa4'
DEBUG = True
