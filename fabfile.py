from fabric.api import *
 
# Configure user, private key, etc. for SFTP deployment
env.user = 'takosuke'
env.hosts = ['31.222.155.138']
env.keyfile = ['$HOME/.ssh/id_rsa']
 
def pack():
    local('python setup.py sdist --formats=gztar', capture=False)
 
def deploy():
    dist = local('python setup.py --fullname', capture=True).strip()
    put('dist/%s.tar.gz' % dist, '/tmp/psc.tar.gz')
 
    # now we're on the remote host from here on out!
    run('mkdir /tmp/psc')
    with cd('/tmp/psc'):
        run('tar zxf /tmp/psc.tar.gz')
        run('mv ' + dist + '/* .')
        sudo('/home/takosuke/public_html/pizzasuicideclub.com/public/flask_PSC/bin/python setup.py install')
 
    sudo('chown -R nginx:nginx /home/takosuke/public_html/pizzasuicideclub.com/public/')
    sudo('rm -rf /tmp/psc /tmp/psc.tar.gz')
 
    # alert uWSGI to reload the project
    sudo('touch /home/takosuke/public_html/pizzasuicideclub.com/public/psc_app/__init__.py')
