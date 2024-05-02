from abc import ABC,abstractmethod
import json
from uuid import uuid4
class SaverFactory(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def add_vacancy(self,vacancy):
        ...
        
    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy_id):
        pass
        
class JsonSaver(SaverFactory):
    def __init__(self):
        self.__vacancies = []
        self.load_vacancies()
    def load_vacancies(self):
        try:
            with open("vacancies.json","r") as f:
                self.__vacancies = json.loads(f.read())
                f.close()
        except FileNotFoundError:
            self.__vacancies = []
        except json.decoder.JSONDecodeError:
            self.__vacancies = []
    def add_vacancy(self,vacancy):
        
        ids_vacancy = {
            "id": len(self.__vacancies),
            "name": vacancy.name,
            "description": vacancy.description,
            "salary": vacancy.salary,
            "URL": vacancy.URL
        }
            
        self.__vacancies.append(ids_vacancy)
        with open("vacancies.json","w") as f:
            f.write(json.dumps(self.__vacancies))
            f.close()
            
    def get_vacancies(self, id):
        return self.__vacancies[id]
    def remove_vacancy(self, vacancy_id):
        for vacancy in self.__vacancies:
            if vacancy["id"] == vacancy_id:
                self.__vacancies.remove(vacancy)
                break

        with open("vacancies.json", "w") as f:
            f.write(json.dumps(self.__vacancies))