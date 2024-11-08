from src.vacancy import Vacancy


def sort_top_vacations(list_: list, n):
    list_.sort(reverse=True)
    return list_[:n]


def sort_by_requirement(list_: list[Vacancy], requirement):
    new_list = []

    for vacancy in list_:
        if requirement in vacancy.requirement:
            new_list.append(vacancy)

    return new_list


