from flask import Blueprint, render_template, flash, redirect, g, url_for, request, session, send_from_directory
from werkzeug import check_password_hash, generate_password_hash
import os, datetime, random

from psc_app import app, psc_db, utilities
from psc_app.users.models import User
from psc_app.posts.models import Post
STATIC = app.config['STATIC']


from decorators import requires_login
from forms  import RegistrationForm, LoginForm, UserForm, DeleteForm, ModifyPasswordForm, UploadProfilePicForm

mod = Blueprint('users', __name__,  url_prefix='/users')



@mod.before_request
def before_request():
    """
    pull user's profile from the database before every request are treated
    """
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id']);
        

@mod.route('/profile/<userId>')
def profile(userId):
    user = g.user
    profile = User.query.get(userId)
    form = UploadProfilePicForm()
    if not profile:
        flash('user doesnt exist')
        return redirect(url_for('pages.userlist'))
    return render_template("users/profile.html",profile = profile, user = user, form = form)






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
            return redirect(url_for('users.profile', userId = user.id))
        flash('wrong wrong email or password or somethign', 'error-message')
    return render_template("users/login.html", form=form)

@mod.route('/logout')
def logout():
    flash('you arrre logged outtt')
    session.pop('user_id', None)
    return redirect(url_for('users.login'))


@mod.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if g.user is not None:
        return redirect(url_for('users.home'))
    if request.method == 'POST' and form.validate():
        
        if User.query.filter_by(username = form.username.data).first():
            flash ('The username already exists idiot')
            return render_template("users/register.html", title = 'register', form = form)
        if User.query.filter_by(email = form.email.data).first():
            flash ('The email has already been registored')
            return render_template("users/register.html", title = 'register', form = form)
        file = form.image.data
        profile_pic = utilities.file_save(file, 'profilepics')
        user = User(username = form.username.data,email = form.email.data,password = generate_password_hash(form.password.data), description = form.description.data, profile_pic = profile_pic, homepage = form.homepage.data, role = form.role.data, zodiac = form.zodiac.data )
        psc_db.session.add(user)
        psc_db.session.commit()
        session['user_id'] = user.id
        flash('well done faggot')
        return redirect(url_for('users.profile', userId = user.id))
    return render_template("users/register.html", title = 'register', form = form)

@mod.route('/registertest', methods=['GET', 'POST'])
def registertest():
    form = RegistrationForm()
    if g.user is not None:
        return redirect(url_for('users.home'))
    if request.method == 'POST' and form.validate():
        return 'yeah'
    return render_template("users/register.html", title = 'register', form = form)
    


@mod.route('/modify/<userId>', methods=['GET', 'POST'])
@requires_login
def modify_profile(userId):
    user = g.user
    profile = User.query.get(userId)
    if user.role != 3 and user.id != int(userId)    :
        flash('what do u think u doing thats not ur profile')
        return redirect(url_for('users.profile', userId = userId))
    form = UserForm()
    if request.method == 'POST' and form.validate():
        if User.query.filter(User.id != userId).filter_by(username = form.username.data).first():
            flash ('The username already exists idiot')
            return render_template("users/modify_profile.html", form = form, user = user)
        if User.query.filter(User.id != userId).filter_by(email = form.email.data).first():
            flash ('The email has already been registored')
            return render_template("users/modify_profile.html", form = form, user = user)
        profile.username = form.username.data
        profile.email = form.email.data
        profile.description = form.description.data
        profile.homepage = form.homepage.data
        profile.role = form.role.data
        profile.zodiac = form.zodiac.data
        psc_db.session.commit()
        return redirect(url_for('users.profile', userId = userId))
    form.username.data = profile.username
    form.email.data = profile.email
    form.description.data = profile.description
    form.homepage.data = profile.homepage
    form.zodiac.data = profile.zodiac
    return render_template("users/modify_profile.html", form = form, user = user)

@mod.route('/modify/password/<userId>', methods=['GET', 'POST'])
@requires_login
def modify_password(userId):
    user = g.user
    form = ModifyPasswordForm()
    if request.method == 'POST' and form.validate():
        old_hashed_password = generate_password_hash(form.old_password.data)
        new_hashed_password = generate_password_hash(form.new_password.data)
        if check_password_hash(user.password, form.old_password.data):
            user = User.query.get(userId)
            user.password = new_hashed_password
            psc_db.session.commit()
            flash('Password has beeen changed')
            return redirect(url_for('users.profile', userId = userId))
    return render_template("users/modify_password.html", form = form, user = user)
    



@mod.route('/delete/<userId>', methods=['GET', 'POST'])
@requires_login
def delete_profile(userId):
    user = g.user
    form = DeleteForm()
    if request.method == 'POST' and form.delete_confirm.data == True:
        profile = User.query.get(userId)
        psc_db.session.delete(profile)
        psc_db.session.commit()
        return redirect(url_for('pages.index'))
    return render_template('users/delete_user.html', form = form, user = user)



