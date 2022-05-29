from flask import Blueprint, request, jsonify

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts/')
def posts_all():
    return jsonify({"content": "Все посты тут"})


@api_blueprint.route('/api/posts/<int:post_id>/')
def posts_one(post_id):
    return jsonify({"content": "Страничка одного поста"})
