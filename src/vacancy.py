from typing import Optional


class Vacancy:
    __slots__ = ["__name", "__requirement", "__salary", "__city"]

    def __init__(self, name: Optional[str], requirement: Optional[str], salary: Optional[float], city: Optional[str]):
        self.__name = name
        self.__requirement = requirement
        self.__salary = salary
        self.__city = city
        self.__validation()

    @classmethod
    def output_vacancies(cls, dictionary: dict) -> "Vacancy":
        return cls(
            **{
                "name": dictionary["name"],
                "requirement": (
                    dictionary["snippet"]["requirement"] if dictionary["snippet"] is not None else dictionary["snippet"]
                ),
                "salary": dictionary["salary"]["from"] if dictionary["salary"] is not None else 0,
                "city": dictionary["address"]["city"] if dictionary["address"] is not None else dictionary["address"],
            }
        )

    def __validation(self) -> None:
        if self.__name is None:
            self.__name = "Не указано"
        if self.__requirement is None:
            self.__requirement = "Не указано"
        if self.__salary is None:
            self.__salary = 0
        if self.__city is None:
            self.__city = "Не указано"

    def __lt__(self, other: "Vacancy") -> bool:
        if other.salary is not None and self.__salary is not None:
            return self.__salary < other.salary
        return False

    def __le__(self, other: "Vacancy") -> bool:
        if other.salary is not None and self.__salary is not None:
            return self.__salary < other.salary
        return False

    def __str__(self) -> str:
        return (
            f"'name': {self.__name}\n"
            f"'requirement': {self.__requirement}\n"
            f"'salary': {self.__salary}\n"
            f"'city': {self.__city}\n"
        )

    @property
    def name(self) -> Optional[str]:
        return self.__name

    @property
    def requirement(self) -> Optional[str]:
        return self.__requirement

    @property
    def salary(self) -> Optional[float]:
        return self.__salary

    @property
    def city(self) -> Optional[str]:
        return self.__city
