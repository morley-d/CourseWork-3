"""
API с двумя эндпоинтами: возврат полного списка постов
                         и возврат одного поста
"""
import logging
from flask import Blueprint, request, jsonify
from app.posts.dao.posts_dao import PostsDAO
from app.posts.dao.comments_dao import CommentsDAO

# from app.posts.clas.post import Post
# import jsonpickle

api_blueprint = Blueprint('api_blueprint', __name__)

posts_dao = PostsDAO('data/posts.json')
comments_dao = CommentsDAO('data/comments.json')

logger = logging.getLogger("basic")


# @api_blueprint.route('/api/posts_as_classes/')
# def posts_as_class_all():
#     jsonpickle.set_encoder_options('json', ensure_ascii=False)
#     logger.debug("Запрошены все посты как классы через API")
#     posts = posts_dao.get_all()
#     posts_as_class = []
#     for post in posts:
#         exemp_post = Post(post['pk'],
#                           post['poster_name'],
#                           post['poster_avatar'],
#                           post['pic'],
#                           post['content'])
#         posts_as_class.append(exemp_post)
#     return jsonpickle.encode(posts_as_class)


@api_blueprint.route('/api/posts/')
def posts_all():
    logger.debug("Запрошены все посты через API")
    posts = posts_dao.get_all()
    return jsonify(posts)


@api_blueprint.route('/api/post/<int:post_pk>/')
def posts_one(post_pk):
    logger.debug(f"Запрошен пост с pk {post_pk} через API")
    post = posts_dao.get_by_pk(post_pk)
    return jsonify(post)
