
from fabric.api import env, run, cd

USERNAME = 'takosuke'
SERVER = '31.222.155.138'
APP_NAME = 'psc_app'
PROJECT_DIR = '/home/takosuke/public_html/pizzasuicideclub.com/public/'
WSGI_SCRIPT = '__init__.py'

env.hosts = ["%s@%s" % (USERNAME, SERVER)]

def deploy():
    with cd(PROJECT_DIR):
        run('git pull')
        run('bin source/activate')
        run('pip install -r requirements.txt')
        run('touch %s' % WSGI_SCRIPT)

