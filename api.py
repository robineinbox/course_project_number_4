from abc import ABC, abstractmethod
from vacancy import Vacancy
import requests
import json


class API(ABC):
    @abstractmethod
    def get_vacancies(self, search_query):
        pass


class HeadHunterAPI(API):
    def get_vacancies(self, search_query):
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": search_query,
            "search_field": "name",
            "vacancy_search_order": 2
        }
        response = requests.get(url, params=params)
        if response.ok:
            data = json.loads(response.text)
            vacancies = []
            for vacancy in data["items"]:
                v = Vacancy(
                    title=vacancy["name"],
                    url=vacancy["alternate_url"],
                    salary=vacancy.get("salary"),
                    description=vacancy.get("snippet").get("responsibility")
                )
                vacancies.append(v)
            return vacancies
        else:
            print("Error: ", response.status_code)
            return []


class SuperJobAPI(API):
    def __init__(self, token):
        self.token = token

    def get_vacancies(self, search_query):
        url = "https://api.superjob.ru/2.0/vacancies/"
        headers = {"X-Api-App-Id": self.token}
        params = {"keyword": search_query}
        response = requests.get(url, headers=headers, params=params)
        if response.ok:
            data = json.loads(response.text)
            vacancies = []
            for vacancy in data["objects"]:
                v = Vacancy(
                    title=vacancy["profession"],
                    url=vacancy["link"],
                    salary=vacancy.get("payment_from"),
                    description=vacancy.get("candidat") or vacancy.get("work")
                )
                vacancies.append(v)
            return vacancies
        else:
            print("Error: ", response.status_code)
            return []