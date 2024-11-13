from src.vacancy import Vacancy


def sort_top_vacations(list_: list, n: int) -> list:
    list_.sort(reverse=True)
    return list_[:n]


def sort_by_requirement(list_: list[Vacancy], requirement: str) -> list:
    new_list = []

    for vacancy in list_:
        if vacancy.requirement is not None:
            if requirement in vacancy.requirement:
                new_list.append(vacancy)

    return new_list
