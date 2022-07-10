from flask import Flask
from utils import load_candidates, formate_candidate

app = Flask(__name__)

# Создаем список кандидатов
candidates = load_candidates()


@app.route("/")
def get_all():
    """
    :return: Возвращает список всех кандидатов
    """
    formatted_candidates = [formate_candidate(candidate) for candidate in candidates]
    formatted_candidates = "\n\n".join(formatted_candidates)
    return "".join(["<pre>", formatted_candidates, "</pre>"])


@app.route("/candidates/<int:pk>/")
def get_by_pk(pk):
    """
    :param pk: pk, который задает пользователь
    :return: Возвращает кандидата по его pk
    """
    for candidate in candidates:
        if candidate["pk"] == pk:
            picture_url = candidate["picture"]
            return "".join([f"<img src='{picture_url}'>", "<pre>", formate_candidate(candidate), "</pre>"])
    return "Нет кандидата с таким PK"


@app.route("/skills/<skill_name>/")
def get_by_skill(skill_name):
    """
    :param skill_name: Навык, который задаёт пользователь
    :return: Возвращает всех кандидатов у которых есть нужный навык
    """
    skilled_candidates = [formate_candidate(candidate) for candidate in candidates if
                          skill_name.lower() in candidate["skills"].lower()]
    skilled_candidates = "\n\n".join(skilled_candidates)
    return "".join(["<pre>", skilled_candidates, "</pre>"])


app.run()
