import pytest
from unittest.mock import mock_open, patch,Mock
from modules.Vacancy import Vacancy
from modules.API import HeadHunterAPI
from modules.saver import JsonSaver


@pytest.fixture
def vacancy():
    return Vacancy("Python Developer", URL="https://hh.tu/1231451512", salary=1000, description="need to super power")



# Tests for HeadHunterAPI
def test_api_get_vacancies():
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies("Python", count=3)
    assert len(hh_vacancies["items"]) == 3

def test_api_get_vacancy_by_id():
    hh_api = HeadHunterAPI()
    hh_vacancy = hh_api.get_vacancy_by_id(93439149)
    assert hh_vacancy["name"] == "Golang разработчик"
    
# Tests for Vacancy
def test_vacancy_init(vacancy):
    assert vacancy.name == "Python Developer"
    assert vacancy.description == "need to super power"
    assert vacancy.salary == 1000
    assert vacancy.URL == "https://hh.tu/1231451512"

def test_init_with_null_salary():
    temp_vacancy = Vacancy("Python Developer", URL="https://hh.tu/1231451512", salary="null", description="need to super power")
    assert temp_vacancy.salary == 0

def test_init_with_dict_salary():
    salary = {"from": 3000, "to": 5000}
    vacancy = Vacancy("Data Scientist", "Machine learning expert", salary, "https://example.com")
    assert vacancy.salary == 4000

def test_init_with_regular_salary():
    vacancy = Vacancy("Product Manager", "Product strategy", 6000, "https://example.com")
    assert vacancy.salary == 6000

def test_vacancy_cast_to_object_list():
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies("Python", count=3)
    vacancies = Vacancy.cast_to_object_list(json_data=hh_vacancies)
    assert len(vacancies) == 3

def test_equals_vacancy(vacancy):
    assert vacancy == Vacancy("Python Developer", URL="https://hh.tu/1231451512", salary=1000, description="need to super power")

def test_less_vacancy(vacancy):
    assert vacancy < Vacancy("Python Developer", URL="https://hh.tu/1231451512", salary=50000, description="need to super power")

def test_greater_vacancy(vacancy):
    assert Vacancy("Python Developer", URL="https://hh.tu/1231451512", salary=50000, description="need to super power") > vacancy
    
    
# JSON Saver tests

def test_load_vacancies_file_not_found():
    with patch("builtins.open", mock_open()) as mock_file:
        mock_file.side_effect = FileNotFoundError
        json_saver = JsonSaver()
        assert json_saver._JsonSaver__vacancies == []

def test_load_vacancies_json_decode_error():
    with patch("builtins.open", mock_open(read_data="invalid json")) as mock_file:
        json_saver = JsonSaver()
        assert json_saver._JsonSaver__vacancies == []

def test_load_vacancies_success():
    with patch("builtins.open", mock_open(read_data='[{"id": 1, "name": "Software Engineer"}]')) as mock_file:
        json_saver = JsonSaver()
        assert json_saver._JsonSaver__vacancies == [{"id": 1, "name": "Software Engineer"}]

def test_add_vacancy(vacancy):
    json_saver = JsonSaver()
    json_saver.add_vacancy(vacancy)
    
    # Additional assertion to check file content
    with open("vacancies.json", "r") as f:
        data = f.read()
        assert "Python Developer" in data
        
def test_get_vacancies_by_index():
    json_saver = JsonSaver()
    first_job = json_saver.get_vacancies(0)
    assert first_job["name"] == "Python Developer"
    
def test_remove_vacancy():
    json_saver = JsonSaver()
    json_saver.remove_vacancy(0)
    
    # Additional assertion to check file content
    with open("vacancies.json", "r") as f:
        data = f.read()
        assert "Python Developer" not in data