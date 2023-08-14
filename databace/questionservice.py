from databace.models import Questions
from databace import db


# Функция добавления вопроса
def add_question(main_text, v1, v2, v3, v4, correct_answer, level):
    new_question = Questions(main_text=main_text, v1=v1, v2=v2,
                             v3=v3, v4=v4, correct_answer=correct_answer, level=level)
    db.session.add(new_question)
    db.session.commit()


# Вывести 20 вопросов
def get_questions(name_level):
    name = Questions.query.filter_by(level=name_level).all()
    return name[:21]


# Проверка ответа пользователя
def check_answer(q_id, user_answer):
    questions = Questions.query.filter_by(id=user_answer)
    if questions.correct_answer == user_answer:
        return True
    return False


