import json


class PostsDAO:
    """ Класс для загрузки данных для постов """

    def __init__(self, path):
        self.path = path

    def load(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.load(file)

    # возвращает все посты
    def get_all(self):
        return self.load()

    # возвращает пост по его идентификатору
    def get_by_pk(self, pk):
        posts = self.get_all()
        for post in posts:
            if post['pk'] == pk:
                return post

    # возвращает посты определенного пользователя
    def get_posts_by_user(self, user_name):
        posts = self.get_all()
        posts_founded = []
        for post in posts:
            if user_name.lower() in post['poster_name'].lower():
                posts_founded.append(post)
        return posts_founded

    # возвращает список словарей по вхождению
    def search(self, query):
        posts = self.get_all()
        matching_posts = []
        for post in posts:
            if query.lower() in post['content'].lower():
                matching_posts.append(post)
        return matching_posts
