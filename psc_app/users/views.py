from flask import Blueprint, render_template, flash, redirect, g, url_for, request, session, send_from_directory
from werkzeug import check_password_hash, generate_password_hash
import os, datetime, random

from psc_app import app, psc_db, utilities
from psc_app.users.models import User
from psc_app.posts.models import Post
from config import STATIC

from decorators import requires_login
from forms  import RegistrationForm, LoginForm

mod = Blueprint('users', __name__,  url_prefix='/users')

@mod.route('/me')
@requires_login
def home():
    return render_template("users/profile.html", user = g.user)


@mod.before_request
def before_request():
    """
    pull user's profile from the database before every request are treated
    """
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id']);
        
        

@mod.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if g.user is not None:
        return redirect(url_for('users.home'))
    if request.method == 'POST' and form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('You are logged in %s' % user.username )
            return redirect(url_for('users.home'))
        flash('wrong wrong email or password or somethign', 'error-message')
    return render_template("users/login.html", form=form)

@mod.route('/logout')
def logout():
    flash('you arrre logged outtt')
    session.pop('user_id', None)
    return redirect(url_for('users.login'))

@mod.route('/test', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        return file.filename
    return render_template('upload.html')

@mod.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        if User.query.filter_by(username = form.username.data).first():
            flash ('The username already exists idiot')
            return render_template("users/register.html", title = 'register', form = form)
        if User.query.filter_by(email = form.email.data).first():
            flash ('The email has already been registored')
            return render_template("users/register.html", title = 'register', form = form)
        profile_pic = utilities.file_save('profilepics')
        user = User(username = form.username.data,email = form.email.data,password = generate_password_hash(form.password.data), description = form.description.data, profile_pic = profile_pic, homepage = form.homepage.data, role = form.role.data, zodiac = form.zodiac.data )
        psc_db.session.add(user)
        psc_db.session.commit()
        session['user_id'] = user.id
        flash('well done faggot')
        return redirect(url_for('users.home'))
    return render_template("users/register.html", title = 'register', form = form)

@mod.route('/members')
@requires_login
def userlist():
    users = models.User.query.all()
    return render_template("userlist.html", title='members', users = users)

@app.route('/request', methods=['GET', 'POST'])
def test():
    form = TestForm()
    if request.method == 'POST':
        return 
    return render_template('users/testform.html', form = form)






