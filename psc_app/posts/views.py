from flask import Blueprint, render_template, flash, redirect, g, url_for, request, session
from datetime import datetime

from psc_app import app, psc_db, utilities


from psc_app.posts.models import Post
from psc_app.users.models import User
from psc_app.users.decorators import requires_login
from config import STATIC

import forms





mod = Blueprint('posts', __name__, static_folder = STATIC, url_prefix='/posts')

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
    form = forms.PostForm()
    if request.method == 'POST' and form.validate():
        user_id = g.user.id
        image = utilities.file_save('images')
        post = Post(title = form.title.data,body = form.body.data, image = image, timestamp = datetime.utcnow(), category = form.category.data, user_id = user_id )
        psc_db.session.add(post)
        psc_db.session.commit()
        flash('well posted mutafuqa')
        return redirect(url_for('pages.index'))
    return render_template("posts/post_create.html", title="write something", form = form)


