from flask import Blueprint, render_template, flash, redirect, g, url_for, request, session, send_from_directory
from datetime import datetime

from psc_app import app, psc_db, utilities

from psc_app.posts.models import Post
from psc_app.users.models import User
from psc_app.users.decorators import requires_login
STATIC = app.config['STATIC']


from forms import PostForm, DeleteForm



mod = Blueprint('posts', __name__, url_prefix='/posts')

@mod.before_request
def before_request():
    """
    pull user's profile from the database before every request are treated
    """
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])

@mod.route('/post', methods=['GET', 'POST'])
@requires_login
def create_post():
    user = g.user
    form = PostForm()
    if request.method == 'POST' and form.validate():
        user_id = g.user.id
        file = form.image.data
        image = utilities.file_save(file, 'images')
        post = Post(title = form.title.data,body = form.body.data, image = image, timestamp = datetime.utcnow(), category = form.category.data, user_id = user_id, front_page = form.front_page.data )
        psc_db.session.add(post)
        psc_db.session.commit()
        flash('well posted mutafuqa')
        return redirect(url_for('pages.index'))
    return render_template("posts/create_post.html", title="write something", user =user, form = form)

@mod.route('/manage', methods=['GET', 'POST'])
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
    user = g.user
    if request.method == 'POST' and form.validate():
        post.title = form.title.data
        post.body = form.body.data
        post.category = form.category.data
        post.front_page = form.front_page.data
        if form.image.data:
            file = form.image.data
            post.image = utilities.file_save(file,'images')
        psc_db.session.add(post)
        psc_db.session.commit()
        return redirect(url_for('posts.manage_posts'))
    form.title.data = post.title
    form.body.data = post.body
    form.category.data = str(post.category)
    form.front_page.data = post.front_page
    return render_template("posts/create_post.html", user = user, form = form)
    


    
