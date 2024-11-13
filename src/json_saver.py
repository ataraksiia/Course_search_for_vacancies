import json
from abc import ABC, abstractmethod
from typing import Any

from src.vacancy import Vacancy


class Saver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def del_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def get_vacancies(self) -> Any:
        pass

    @abstractmethod
    def save_to_file(self, vacancies: list) -> Any:
        pass


class JSONSaver(Saver):
    def __init__(self, file_path: str = "vac.json"):
        self.__file_path = file_path
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump([], file)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        data = {
            "name": vacancy.name,
            "requirement": vacancy.requirement,
            "salary": vacancy.salary,
            "city": vacancy.city,
        }
        json_data = self.get_vacancies()
        json_data.append(data)
        self.save_to_file(json_data)

    def del_vacancy(self, vacancy: Vacancy) -> None:
        data = {
            "name": vacancy.name,
            "requirement": vacancy.requirement,
            "salary": vacancy.salary,
            "city": vacancy.city,
        }
        json_data = self.get_vacancies()
        json_data.remove(data)
        self.save_to_file(json_data)

    def get_vacancies(self) -> Any:
        with open(self.__file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_to_file(self, vacancies: list) -> Any:
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    @property
    def file_path(self) -> Any:
        return self.__file_path
