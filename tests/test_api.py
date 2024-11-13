from unittest.mock import Mock, patch

from src.api import HH


def test_load_vacancies() -> None:
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {
            "items": [
                {
                    "name": "Фронтенд разработчик NextReact",
                    "requirement": "Опыт работы с Next.js и React от 2 лет.",
                    "salary": 130_000,
                    "city": "Ташкент",
                }
            ]
        }
        mock_get.return_value = mock_response

        hh1 = HH()
        hh1.load_vacancies("Фронтенд", 1)

        assert hh1.vacancies == [
            {
                "name": "Фронтенд разработчик NextReact",
                "requirement": "Опыт работы с Next.js и React от 2 лет.",
                "salary": 130_000,
                "city": "Ташкент",
            }
        ]
