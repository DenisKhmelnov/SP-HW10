from flask import Flask
import json

app = Flask(__name__)


def load_candidates():
    """
    :return: Возвращает список со всеми кандидатами из файла JSON
    """
    with open("candidates.json") as file:
        candidates_list = json.load(file)
        return candidates_list


def formate_candidate(candidate):
    """
    :param candidate:
    :return: Возвращает форматированную строку с заданным кандидатом
    """
    return f"""Имя кандидата - {candidate["name"]}
Позиция кандидата - {candidate["position"]}
Навыки кандидата: {candidate["skills"]}"""


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
    :return: Вовращает сандидата по его pk
    """
    for candidate in candidates:
        if candidate["pk"] == pk:
            return "".join(["<pre>", formate_candidate(candidate), "</pre>"])
    return "Нет кандидата с таким PK"

@app.route("/skills/<skill_name>/")
def get_by_skill(skill_name):
    """
    :param skill_name: Навык, который задаёт пользователь
    :return: Возвращает всех кандидатов у которых есть нужный навык
    """
    skilled_candidates = [formate_candidate(candidate) for candidate in candidates if skill_name.lower() in candidate["skills"].lower()]
    skilled_candidates = "\n\n".join(skilled_candidates)
    return "".join(["<pre>", skilled_candidates, "</pre>"])


app.run()
