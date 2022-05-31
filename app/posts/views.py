from flask import Blueprint, render_template, request
from .dao.posts_dao import PostsDAO

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='../../templates')
posts_dao = PostsDAO('data/posts.json')


@posts_blueprint.route('/')
def posts_all():
    try:
        posts = posts_dao.get_all()
        return render_template('index.html', posts=posts)
    except:
        render_template("Что то пошло не так")
    return "Все посты тут"


@posts_blueprint.route('/posts/<int:post_id>/')
def posts_one(post_id):
    return "Страничка одного поста"


@posts_blueprint.route('/search/')
def posts_search():
    return "Поиск по постам"


@posts_blueprint.route('/users/<username>/')
def posts_by_users(username):
    return "Поиск по постам пользователя"
