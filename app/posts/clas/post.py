""" Для опробования сериализации объектов """

class Post:

    def __init__(self, pk, poster_name, poster_avatar, pic, content):
        self.pk = pk
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content

    def __repr__(self):
        return f"{self.poster_name} {self.pk}"
