import json


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
