class Vacancy():
    __slots__ = ["__name", "__requirement", "__salary", "__city"]

    def __init__(self, name: str, requirement: str, salary: float, city: str):
        self.__name = name
        self.__requirement = requirement
        self.__salary = salary
        self.__city = city
        self.__validation()

    @classmethod
    def output_vacancies(cls, dictionary: dict):
        return cls(dictionary["name"],
                   dictionary['snippet']["requirement"] if dictionary['snippet'] is not None else None,
                   dictionary["salary"]['from'] if dictionary["salary"] is not None else 0,
                   dictionary['address']["city"] if dictionary['address'] is not None else None)

    def __validation(self):
        if self.__name is None:
            self.__name = "Не указано"
        if self.__requirement is None:
            self.__requirement = "Не указано"
        if self.__salary is None:
            self.__salary = 0
        if self.__city is None:
            self.__city = "Не указано"

    def __lt__(self, other):
        return self.__salary < other.salary

    def __le__(self, other):
        return self.__salary <= other.salary

    def __str__(self):
        return (f"'name': {self.__name}\n"
                f"'requirement': {self.__requirement}\n"
                f"'salary': {self.__salary}\n"
                f"'city': {self.__city}\n")

    @property
    def name(self):
        return self.__name

    @property
    def requirement(self):
        return self.__requirement

    @property
    def salary(self):
        return self.__salary

    @property
    def city(self):
        return self.__city

