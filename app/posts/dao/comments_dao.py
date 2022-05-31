import json


class CommentsDAO:

    """ Класс для работы с данными для комментариев """

    def __init__(self, path):
        self.path = path

    # загрузка всех комментариев
    def load_comments(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.load(file)

    # получение комментария к определенному посту
    def get_by_post_pk(self, post_pk):
        comments = self.load_comments()
        comments_by_pk = []
        for comment in comments:
            if comment["post_pk"] == post_pk:
                comments_by_pk.append(comment)
        return comments_by_pk
