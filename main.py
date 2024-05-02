from abc import ABC,abstractmethod

from modules.API import HeadHunterAPI
from modules.Vacancy import Vacancy
from modules.saver import JsonSaver

def UserClient():
    
    query = input("Введите поисковый запрос для запроса вакансий из hh.ru: ")

    n = int(input("Введите количество вакансий для вывода: "))
    
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(query, count=n)
    vacancies_data = Vacancy.cast_to_object_list(json_data=hh_vacancies)
    for data in vacancies_data:
        print(data)
    
    
    print(f"Топ {n} вакансий по зарплате:")
    sorted_vacancies = sorted(vacancies_data, key=lambda x: x.salary, reverse=True)
    for idx, vacancy in enumerate(sorted_vacancies, start=1):
        print(f"{idx}. {vacancy.name} - {vacancy.salary} rub")

    keyword = input("Введите ключевое слово для поиска в описании вакансий: ")
    detail_vacancies = []
 
    for vacancy in hh_vacancies["items"]:
        detail_vacancies.append(hh_api.get_vacancy_by_id(vacancy["id"]))
        
    if detail_vacancies:
        print(f"\nВакансии с ключевым словом '{keyword}' в описании:")
        for idx, vacancy in enumerate(detail_vacancies, start=1):
            if keyword in vacancy['description']:
                print(f"{idx}. {vacancy['name']} - {vacancy['description']}")
            
    else:
        print(f"По вашему запросу вакансий с ключевым словом '{keyword}' не найдено.")
UserClient()