from abc import ABC, abstractmethod
from typing import Any, List

import requests


class VacancyAPI(ABC):
    @abstractmethod
    def load_vacancies(self, keyword: str) -> None:
        pass


class HH(VacancyAPI):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self) -> None:
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params: Any = {"text": "", "page": 0, "per_page": 100, "search_fields": ["title", "skills"]}
        self.__vacancies: List[dict] = []

    def load_vacancies(self, keyword: str, n: int = 20) -> None:
        self.__params["text"] = keyword

        while self.__params.get("page") != n:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

    @property
    def url(self) -> str:
        return self.__url

    @property
    def headers(self) -> dict:
        return self.__headers

    @property
    def params(self) -> Any:
        return self.__params

    @property
    def vacancies(self) -> list:
        return self.__vacancies
