from db import get_db
from db.models import PostPhoto, UserPost, Comment, Hashtag

"""
UserPost functions
"""
# Cоздания поста
# Изменения поста
# Удаление поста
# Получение всех постов
# ПОлучение определенного поста

"""
Comment functions
"""
# Создание коммента
def create_comment_db(user_id, post_id, text, reg_date):
    db = next(get_db())
    new_comment = Comment(user_id=user_id, post_id=post_id, text=text, reg_date=reg_date)
    db.add(new_comment)
    db.commit()
# Полчение коммента по его айди
def get_exact_comment_db(comment_id):
    db=next(get_db())
    exact_comment = db.query(Comment).filter_by(id=comment_id).first()
    return exact_comment
# Получение всех комментов по айди поста
def get_all_comments_db(post_id):
    db=next(get_db())
    all_comments = db.query(Comment).filter_by(post_id=post_id).all()
    return all_comments
# Изменение коммента
def edit_comment_db(comment_id, new_text):
    db=next(get_db())
    edit_comment = db.query(Comment).filter_by(id=comment_id).first()
    if edit_comment is None:
        return False
    edit_comment.text = new_text
    db.commit()
    return True
# Удаление коммента
def delete_comment_db(comment_id):
    db = next(get_db())
    delete_comment = db.query(Comment).filter_by(id=comment_id).first()
    if delete_comment:
        db.delete(delete_comment)
        db.commit()
        return True
    return False

"""
Hashtag functions
"""
# Создание хэштега
# Получение хэштега по названию
# Получение всех хэштегов
# Удаление хэштега
# Изменение хэштега
