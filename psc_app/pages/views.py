from flask import Blueprint, render_template, flash, redirect, g, url_for, request, session
from flask.ext.sqlalchemy import Pagination
from micawber.providers import bootstrap_basic
from micawber.contrib.mcflask import add_oembed_filters

from psc_app import app, psc_db, utilities
from psc_app.posts.models import Post
from psc_app.users.models import User
from psc_app.users.decorators import requires_login
from config import  POSTS_PER_PAGE


mod = Blueprint('pages', __name__)

oembed_providers = bootstrap_basic()
add_oembed_filters(app, oembed_providers)


@mod.before_request
def before_request():
    """
    pull user's profile from the database before every request are treated
    """
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


@mod.route('/test')
def test():
    user = g.user
    posts = Post.query.join(User).filter(User.id == user.id).order_by(Post.timestamp.desc())
    return render_template("pages/postlist.html", title='Home Page of the Pizza Suicide Club', posts = posts, user = user)



@mod.route('/permalink/<int:postId>')
def permalink(postId):
    user = g.user
    post = Post.query.get(postId)
    return render_template("pages/permalink.html", title='Home Page of the Pizza Suicide Club', post = post, user = user)

@mod.route('/')
@mod.route('/page/<int:page>')
def index(page = 1):
    
    current_page = 'pages.index'
    user = g.user
    posts = Post.query.join(User).filter(User.role != 0).order_by(Post.timestamp.desc()).paginate(page, POSTS_PER_PAGE, False)
    return render_template("pages/postlist.html", title='Home Page of the Pizza Suicide Club', current_page = current_page, posts = posts, user = user)

@mod.route('/events')
@mod.route('/events/page/<int:page>')
def events(page = 1):
    current_page = 'pages.events'
    user = g.user
    posts = Post.query.filter_by(category = 1).join(User).filter(User.role != 0).order_by(Post.timestamp.desc()).paginate(page, POSTS_PER_PAGE, False)
    return render_template("pages/postlist.html", title='Events of the Pizza Suicide Club', current_page = current_page, posts = posts, user = user)
    
    
@mod.route('/releases')
@mod.route('/releases/page/<int:page>')
def releases(page = 1):
    current_page = 'pages.releases'
    user = g.user
    posts = Post.query.filter_by(category = 3).join(User).filter(User.role != 0).order_by(Post.timestamp.desc()).paginate(page, POSTS_PER_PAGE, False)
    return render_template("pages/postlist.html", title='Events of the Pizza Suicide Club', current_page = current_page, posts = posts, user = user)
    

@mod.route('/guests')
@mod.route('/guests/page/<int:page>')
def guests(page = 1):
    current_page = 'pages.guests'
    user = g.user
    posts = Post.query.join(User).filter(User.role == 0).order_by(Post.timestamp.desc()).paginate(page, POSTS_PER_PAGE, False)
    return render_template("pages/postlist.html", title='Dear Guests of the Pizza Suicide Club', current_page = current_page,posts = posts, user = user)



