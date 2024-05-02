from abc import ABC,abstractmethod
import requests

class AbstractAPI(ABC):
     
    @abstractmethod
    def get_vacancies(self,keyword,area:int=1556,count:int=10):
        '''
            Получение вакансий с hh.ru в формате JSON
            Parameters:
                keyword(str): ключевое слово для поиска
                area(int):  код региона, по умолчанию Руспублика Мордовия
                count(int): количество вакансий, по умолчанию 10
        '''
        pass


class HeadHunterAPI(AbstractAPI):
    def __init__(self):
        self.base_url = "https://api.hh.ru/vacancies"
    
    def get_vacancies(self,keyword,area:int=1556,count:int=10):
        req = requests.get(f"{self.base_url}?text={keyword}&area={area}&per_page={count}")
        return req.json()

    def get_vacancy_by_id(self,id):
        req = requests.get(f"{self.base_url}/{id}")
        return req.json()
