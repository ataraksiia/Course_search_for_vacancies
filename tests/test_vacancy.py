from src.vacancy import Vacancy


def test_vacancy__validation() -> None:
    vac = Vacancy(
        **{
            "name": None,
            "requirement": None,
            "salary": None,
            "city": None,
        }
    )
    assert vac.name == "Не указано"
    assert vac.salary == 0
    assert vac.requirement == "Не указано"
    assert vac.city == "Не указано"


def test_output_vacancies() -> None:
    vac = Vacancy.output_vacancies(
        {
            "id": "110719142",
            "premium": False,
            "name": "Водитель-экспедитор",
            "department": None,
            "has_test": False,
            "response_letter_required": True,
            "area": {"id": "160", "name": "Алматы", "url": "https://api.hh.ru/areas/160"},
            "salary": {"from": 500000, "to": 750000, "currency": "KZT", "gross": False},
            "type": {"id": "open", "name": "Открытая"},
            "address": None,
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2024-11-12T04:39:41+0300",
            "created_at": "2024-11-12T04:39:41+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=110719142",
            "show_logo_in_search": None,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/110719142?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/110719142",
            "relations": [],
            "employer": {
                "id": "10558890",
                "name": "Handy Yummy",
                "url": "https://api.hh.ru/employers/10558890",
                "alternate_url": "https://hh.ru/employer/10558890",
                "logo_urls": {
                    "original": "https://img.hhcdn.ru/employer-logo-original/1199176.JPG",
                    "90": "https://img.hhcdn.ru/employer-logo/6417153.jpeg",
                    "240": "https://img.hhcdn.ru/employer-logo/6417154.jpeg",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10558890",
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Только ВОДИТЕЛИ-ЭКСПЕДИТОРЫ С ОПЫТОМ РАБОТЫ.",
                "responsibility": "Обязанности: доставлять товар в торговые точки (магазины, базары, регион).",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "professional_roles": [{"id": "21", "name": "Водитель"}],
            "accept_incomplete_resumes": True,
            "experience": {"id": "between3And6", "name": "От 3 до 6 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    )
    assert vac.name == "Водитель-экспедитор"
