import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request, abort
from .dao.posts_dao import PostsDAO
from .dao.comments_dao import CommentsDAO

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='../../templates')
posts_dao = PostsDAO('data/posts.json')
comments_dao = CommentsDAO('data/comments.json')

logger = logging.getLogger("basic")


@posts_blueprint.route('/')
def posts_all():
    logger.debug("Запрошены все посты")
    try:
        posts = posts_dao.get_all()
        return render_template('index.html', posts=posts)
    except:
        render_template("Что то пошло не так")
    return "Все посты тут"


@posts_blueprint.route('/posts/<int:post_pk>/')
def posts_one(post_pk):
    logger.debug(f"Запрошены пост {post_pk}")
    try:
        post = posts_dao.get_by_pk(post_pk)
        comments = comments_dao.get_by_post_pk(post_pk)
    except (JSONDecodeError, FileNotFoundError) as error:
        return render_template('error.html', error=error)
    except BaseException as e:
        return render_template('error.html', error="Неизвестная ошибка")
    else:
        if post is None:
            abort(404)
        return render_template("post.html", post=post, comments=comments)


@posts_blueprint.route('/search/')
def posts_search():
    query = request.args.get('s', '')
    logger.debug(f'Запрошен поиск по "{query}"')
    if query != "":
        posts = posts_dao.search(query)
    else:
        posts = []
    return render_template('search.html', query=query, posts=posts)


@posts_blueprint.route('/users/<username>/')
def posts_by_users(username):
    posts = posts_dao.get_posts_by_user(username)
    logger.debug(f'Запрошены посты пользователя"{username}"')
    return render_template('user-feed.html', username=username, posts=posts)


@posts_blueprint.route('/tag/<tagname>/')
def posts_for_tag(tagname):
    posts = posts_dao.search_for_tags(tagname)
    return render_template('tag.html', tagname=tagname, posts=posts)


@posts_blueprint.errorhandler(404)
def post_error(e):
    return "Такой пост не найден", 404
