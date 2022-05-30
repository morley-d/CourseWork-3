import pytest

from app.posts.dao.posts_dao import PostsDAO


class TestPostsDAO:
    @pytest.fixture
    def posts_dao(self):
        return PostsDAO("../../../data/posts.json")

    # Получение всех постов

    def test_get_all_check_type(self, posts_dao):
        posts = posts_dao.get_all()
        assert type(posts) == list, "Список постов доолжен быть списком"
        assert type(posts[0]) == dict, "Каждый пост должен быть словарем"

    def test_get_all_has_keys(self, posts_dao):
        posts = posts_dao.get_all()
        first_post = posts[0]
        keys_expected = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
        first_post_keys = set(first_post.keys())
        assert first_post_keys == keys_expected, "Полученные ключи не верны"

    # Получение одного поста

    def test_get_one_check_type(self, posts_dao):
        post = posts_dao.get_by_pk(1)
        assert type(post) == dict

