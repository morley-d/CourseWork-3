import json


def load_all_posts_data():
    try:
        with open("data/posts.json", 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(e)


def get_posts_by_user(posts, user_name):
    posts_founded = []
    for post in posts:
        if user_name.lower() in post['poster_name'].lower():
            posts_founded.append(post)
    return posts_founded


# def save_image(picture):
#     allowed_type = ["jpg", "jpeg", "png", "img", "gif"]
#     picture_type = picture.filename.split('.')[-1]
#     if picture_type not in allowed_type:
#         raise WrongImageType("Неверный формат файла")
#     picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
#     picture.save(picture_path)
#     return picture_path


# def add_post(post_list, post):
#     post_list.append(post)
#     with open(POST_PATH, 'w', encoding='utf-8') as file:
#         json.dump(post_list, file)

print(load_json_posts_data())
