import pytest as pytest

from app.api.views import logger
from run import app


class TestAPI:

    @pytest.fixture
    def response(self):
        return app.test_client().get('/api/posts/', follow_redirects=True)

    @pytest.fixture
    def keys_expected(self):
        return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    # Тесты получения данных для всех постов
    def test_api_all_posts_status_code(self, response):
        assert response.status_code == 200, "Статус код неверный"
        assert response.mimetype == "application/json", "Получен не JSON"

    def test_api_all_posts_type_count_content(self, response):
        assert type(response.json) == list, "Получен не список"
        assert len(response.json) == 8, "Получено неверное количество элементов"

    def test_api_all_posts_type_check_keys(self, keys_expected, response):
        # response = app.test_client().get('/api/posts/', follow_redirects=True)
        first_post_keys = set(response.json[0].keys())
        assert keys_expected == first_post_keys, "Полученные ключи не верны"

    # Тесты получения данных для одного поста
    def test_api_one_post_status_code(self, response):
        assert response.status_code == 200, "Статус код неверный"
        assert response.mimetype == "application/json", "Получен не JSON"

    def test_api_one_post_type_check_keys(self, keys_expected):         # TODO: Почему при использовании фикстуры response оказывается списком?
        response = app.test_client().get('/api/post/1/', follow_redirects=True)
        # logger.debug(response.json)
        first_post_keys = set(response.json.keys())
        assert keys_expected == first_post_keys, "Полученные ключи не верны"
