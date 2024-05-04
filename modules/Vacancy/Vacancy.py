from statistics import mean


class Vacancy:
    __slots__ = ['name', 'description', 'salary', 'URL']

    def __init__(self, name, description, salary, URL):
        self.name = name
        self.description = description
        if salary == "null" or salary is None:
            self.salary = 0  # или "Зарплата не указана"
        elif isinstance(salary, dict):
            self.salary = int(f"{mean([salary['from'], salary['to']])}")
        else:
            self.salary = salary
        self.URL = URL

    @staticmethod
    def cast_to_object_list(json_data):

        vacancies = []
        for vacancy in json_data["items"]:
            vacancies.append(Vacancy(vacancy["name"],
                                     vacancy["snippet"]["requirement"],
                                     vacancy["salary"],
                                     vacancy["alternate_url"]))
        return vacancies

    def __eq__(self, value: object) -> bool:
        return self.salary == value.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __str__(self):
        return f"Название вакансии: {self.name}\
            \nОписание вакансии: {self.description}\
            \nЗарплата: {self.salary}\nСсылка на вакансию: {self.URL}\n"
