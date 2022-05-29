from flask import Blueprint, render_template, request

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')


@posts_blueprint.route('/')
def posts_all():
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
