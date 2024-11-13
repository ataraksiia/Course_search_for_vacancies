# Программа, которая получает информацию о вакансиях с платформы hh.ru в России

### В проекте созданы:

##### В модулe api.py:
* Абстрактный класс для работы с API сервиса с вакансиями **VacancyAPI(ABC)**.
  * Класс, наследующийся от абстрактного класса, который подключается к API и получает вакансии **HH(VacancyAPI)**.

##### В модулe vacancy.py:
* Класс для работы с вакансиями **Vacancy**. Класс сравнивает вакансий между собой по зарплате и валидирует данные.

##### В модулe json_saver.py:
* Абстрактный класс для работы с файлами Saver(ABC).
  * Класс для сохранения информации о вакансиях в JSON-файл **JSONSaver(Saver)**. 
  
##### В модулe utils.py:
* Функции sort_top_vacations и sort_by_requirement, которые сортируют по количеству и описанию.

##### В пакете tests:
* Тесты для функций.

##### В модулe main.py:
* Функция для взаимодействия с пользователем. 