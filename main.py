from src.api import HH
from src.json_saver import JSONSaver
from src.utils import sort_by_requirement, sort_top_vacations
from src.vacancy import Vacancy


def main() -> None:
    user_input = input("Введите вакансию:\n")
    hh = HH()
    hh.load_vacancies(user_input)
    new_list = []
    for vac in hh.vacancies:
        new_list.append(Vacancy.output_vacancies(vac))
    user_input = input("Нужно ли сортировать вакансии (да/нет)?\n")

    if user_input.lower().strip() == "да":
        n = int(input("Сколько вакансии нужно вернуть?\n"))
        new_list = sort_top_vacations(new_list, n)
    user_input = input("Нужно ли фильтровать (да/нет)?\n")

    if user_input.lower().strip() == "да":
        requirement = input("Введите запрос, который хотите видеть в описании:\n")
        new_list = sort_by_requirement(new_list, requirement)

    user_input = input("Нужно ли сохранить в json (да/нет)?\n")
    if user_input.lower().strip() == "да":
        file = input("В какой файл сохранять?\n")
        saver = JSONSaver(file)
        for item in new_list:
            saver.add_vacancy(item)
    else:
        print(*new_list, sep="\n")


if "__main__" == __name__:
    main()
