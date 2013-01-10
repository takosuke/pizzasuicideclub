from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
psc_db = SQLAlchemy(app)

import filters

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
    

app.jinja_env.filters['nl2br'] = filters.nl2br
app.jinja_env.filters['datetimeformat'] = filters.datetimeformat

from psc_app.users.views import mod as usersModule
app.register_blueprint(usersModule)
from psc_app.posts.views import mod as postsModule
app.register_blueprint(postsModule)
from psc_app.pages.views import mod as pagesModule
app.register_blueprint(pagesModule)






