import json


class PostsDAO:
    """ Класс для работы с данными для постов """

    def __init__(self, path):
        self.path = path

    def load(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.load(file)

    # возвращает все посты
    def get_all(self):
        posts = self.load()
        posts_with_tags = self.replace_tags_for_link(posts)
        return posts_with_tags

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

    # возвращает список словарей по тэгу
    def search_for_tags(self, tag):
        posts = self.get_all()
        matching_posts = []
        for post in posts:
            words_list = post["content"].split()
            for word in words_list:
                if tag in word:
                    matching_posts.append(post)
                    break
        return matching_posts

    def create_tags(self, text):
        words_list = text.split()
        for index in range(len(words_list)):
            word = words_list[index]
            if word.startswith('#'):
                words_list[index] = f'<a href="/tag/{word[1:]}">{word}</a>'
        words_list = " ".join(words_list)
        return words_list

    def replace_tags_for_link(self, posts):
        for post in posts:
            new_content = self.create_tags(post["content"])
            post["content"] = new_content
        return posts

