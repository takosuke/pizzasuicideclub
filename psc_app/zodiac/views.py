from flask import Blueprint, render_template, flash, redirect, g, url_for, request, session, send_from_directory
from datetime import datetime

from psc_app import app, psc_db

from psc_app.zodiac.models import Zodiac
from psc_app.users.models import User
from psc_app.users.decorators import requires_login

from forms import ZodiacForm



mod = Blueprint('zodiac', __name__, url_prefix='/zodiac')

@mod.before_request
def before_request():
    """
    pull user's profile from the database before every request are treated
    """
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])

@mod.route('/post/<sign>', methods=['GET', 'POST'])
@requires_login
def update_zodiac(sign):
    form = ZodiacForm()
    if request.method == 'POST' and form.validate():
        user_id = g.user.id
        zodiac = Zodiac(sign = int(sign), body = form.body.data, timestamp = datetime.utcnow())
        psc_db.session.add(zodiac)
        psc_db.session.commit()
        flash('well posted mutafuqa')
        return redirect(url_for('pages.zodiac'))
        

    return render_template("zodiac/update_zodiac.html", title="write something", form = form)

'''@mod.route('/manage', methods=['GET', 'POST'])
@requires_login
def manage_posts():
    user = g.user
    
    posts = Post.query.join(User).filter(User.id == user.id).order_by(Post.timestamp.desc())
    return render_template("posts/manage_posts.html", user = user, posts = posts)
    
@mod.route('/delete/<postId>', methods=['GET', 'POST'])
@requires_login
def delete(postId):
    form = DeleteForm()
    if request.method == 'POST' and form.delete_confirm.data == True:
        post = Post.query.get(postId)
        psc_db.session.delete(post)
        psc_db.session.commit()
        return redirect(url_for('posts.manage_posts'))
    return render_template('posts/delete_post.html', form = form)
    

@mod.route('/modify/<postId>', methods=['GET', 'POST'])
@requires_login
def modify(postId):
    post = Post.query.get(postId)
    form = PostForm()
    if request.method == 'POST' and form.validate():
        post.title = form.title.data
        post.body = form.body.data
        post.category = form.category.data
        post.front_page = form.front_page.data
        post.image = form.image.data
        if request.files['file']:
            post.image = utilities.file_save('images')
        psc_db.session.add(post)
        psc_db.session.commit()
        return redirect(url_for('posts.manage_posts'))
    form.title.data = post.title
    form.body.data = post.body
    form.category.data = str(post.category)
    form.front_page.data = post.front_page
    return render_template("posts/create_post.html", form = form)
    '''
    


    
