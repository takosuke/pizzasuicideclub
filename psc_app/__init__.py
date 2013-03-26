from flask import Flask, render_template, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
psc_db = SQLAlchemy(app)
UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']

import filters

if app.config['DEBUG'] == False:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS, 'microblog failure', credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
    
@app.errorhandler(505)
def internal_error(error):
    db.session.rollback()
    return render_template('505.html'), 505
    
@app.route('/cayampa/<path:filename>')
def uploads(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
    

app.jinja_env.filters['nl2br'] = filters.nl2br
app.jinja_env.filters['datetimeformat'] = filters.datetimeformat

from psc_app.users.views import mod as usersModule
app.register_blueprint(usersModule)
from psc_app.posts.views import mod as postsModule
app.register_blueprint(postsModule)
from psc_app.pages.views import mod as pagesModule
app.register_blueprint(pagesModule)
from psc_app.zodiac.views import mod as zodiacModule
app.register_blueprint(zodiacModule)





