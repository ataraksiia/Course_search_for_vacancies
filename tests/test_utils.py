from pytest import fixture

from src.utils import sort_by_requirement, sort_top_vacations
from src.vacancy import Vacancy


@fixture()
def data() -> list:
    return [Vacancy("", "Повар", 10_000, ""), Vacancy("", "", 20_000, ""), Vacancy("", "", 1_000, "")]


def test_sort_top_vacations(data: list) -> None:
    assert sort_top_vacations(data, 1)[0].salary == 20_000


def test_sort_by_requirement(data: list) -> None:
    assert sort_by_requirement(data, "Повар")[0].salary == 10_000
