import json


class PostsDAO:
    """ Класс для работы с данными для постов """

    def __init__(self, path):
        self.path = path

    # загрузка данных из файла
    def load(self):
        with open(f"{self.path}", 'r', encoding='utf-8') as file:
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

print()

