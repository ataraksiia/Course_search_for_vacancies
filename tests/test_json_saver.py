import json

from pytest import fixture

from src.json_saver import JSONSaver
from src.vacancy import Vacancy


@fixture
def data() -> "Vacancy":
    vac = Vacancy("Фронтенд разработчик NextReact", "Опыт работы с Next.js и React от 2 лет.", None, "Ташкент")
    return vac


def test_add_vacancy(data: Vacancy) -> None:
    js_sev = JSONSaver("test.json")
    js_sev.add_vacancy(data)
    with open("test.json", "r", encoding="utf-8") as file:
        assert json.load(file) == [
            {
                "name": "Фронтенд разработчик NextReact",
                "requirement": "Опыт работы с Next.js и React от 2 лет.",
                "salary": 0.0,
                "city": "Ташкент",
            }
        ]


def test_del_vacancy(data: Vacancy) -> None:
    js_sev = JSONSaver("test.json")
    js_sev.add_vacancy(data)
    js_sev.del_vacancy(data)
    with open("test.json", "r", encoding="utf-8") as file:
        assert json.load(file) == []
