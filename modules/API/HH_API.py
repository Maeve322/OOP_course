from abc import ABC, abstractmethod
import requests


class AbstractAPI(ABC):

    @abstractmethod
    def get_vacancies(self, keyword, area: int = 1556, count: int = 10):

        pass


class HeadHunterAPI(AbstractAPI):
    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword, area: int = 1556, count: int = 10):
        """
        Fetch vacancies from HeadHunter API based on the keyword,
        area, and count.

        Parameters:
        keyword (str): Keyword to search for in vacancy descriptions.
        area (int, optional): Area code to filter vacancies.
        Default is 1556 (Russia, Republic of Mordovia).
        count (int, optional): Number of vacancies to fetch. Default is 10.

        Returns:
        dict: JSON response from the HeadHunter API.
        """
        req = requests.get(f"{self.__base_url}?text={keyword}\
                           &area={area}&per_page={count}")
        return req.json()

    def get_vacancy_by_id(self, id):
        """
        Fetch a vacancy by its ID from the HeadHunter API.

        Parameters:
        id (str): ID of the vacancy to fetch.

        Returns:
        dict: JSON response from the HeadHunter API.
        """
        req = requests.get(f"{self.__base_url}/{id}")
        return req.json()
