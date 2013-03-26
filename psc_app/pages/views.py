from flask import Blueprint, render_template, flash, redirect, g, url_for, request, session
from flask.ext.sqlalchemy import Pagination
from micawber.providers import bootstrap_basic
from micawber.contrib.mcflask import add_oembed_filters

from psc_app import app, psc_db, utilities
from psc_app.posts.models import Post
from psc_app.users.models import User
from psc_app.zodiac.models import Zodiac
from psc_app.users.decorators import requires_login
POSTS_PER_PAGE = app.config['POSTS_PER_PAGE']




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


@mod.route('/permalink/<postId>')
def permalink(postId):
    user = g.user
    post = Post.query.get(postId)
    if post:
        return render_template("pages/permalink.html", title=post.title, post = post, user = user)
    else:
        return render_template("404.html", user = user)
    
@mod.route('/')
@mod.route('/page/<int:page>')
def index(page = 1):
    current_page = 'pages.index'
    user = g.user
    posts = Post.query.join(User).filter(User.role != 0).order_by(Post.timestamp.desc()).paginate(page, POSTS_PER_PAGE, False)
    headlines = Post.query.filter(Post.front_page == True).join(User).filter(User.role != 0).filter(Post.front_page == False).order_by(Post.timestamp.desc()).limit(10).all()
    return render_template("pages/postlist.html", title='Home Page of the Pizza Suicide Club', current_page = current_page, posts = posts, user = user, headlines = headlines)
    


@mod.route('/news')
@mod.route('/news/page/<int:page>')
def news(page = 1):
    current_page = 'pages.news'
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

@mod.route('/zodiac')
def zodiac():
    user = g.user
    #next line pulls users from db to compare signs
    users = User.query.all()
    zodiacs = []
    for x in range (0,12):
        sign = Zodiac.query.filter(Zodiac.sign == x).order_by(Zodiac.timestamp.desc()).first()
        zodiacs.append(sign)
    return render_template("pages/zodiac.html", title='Your Pizza Suicide Zodiac', zodiacs = zodiacs, user = user, users = users)
    
@mod.route('/members')
def userlist():
    user = g.user
    users = User.query.all()
    return render_template("users/userlist.html", title='members', user = user, users = users)

    


