import json
from src.vacancy import Vacancy
from abc import ABC, abstractmethod


class Saver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def del_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def save_to_file(self, vacancies):
        pass


class JSONSaver(Saver):
    def __init__(self, file_path: str = 'vacancies.json'):
        self.__file_path = file_path
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump([], file)

    def add_vacancy(self, vacancy: Vacancy):
        data = {"name": vacancy.name, "requirement": vacancy.requirement,
                "salary": vacancy.salary, "city": vacancy.city}
        json_data = self.get_vacancies()
        json_data.append(data)
        self.save_to_file(json_data)

    def del_vacancy(self, vacancy: Vacancy):
        data = {"name": vacancy.name, "requirement": vacancy.requirement,
                "salary": vacancy.salary, "city": vacancy.city}
        json_data = self.get_vacancies()
        json_data.remove(data)
        self.save_to_file(json_data)

    def get_vacancies(self):
        with open(self.__file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def save_to_file(self, vacancies):
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    @property
    def file_path(self):
        return self.__file_path
