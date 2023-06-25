from abc import ABC, abstractmethod
import json

from vacancy import Vacancy


class VacancyFile(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_criteria(self, criteria):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(VacancyFile):
    def __init__(self, file_path):
        self.file_path = file_path

    def add_vacancy(self, vacancy):
        with open(self.file_path, "r") as f:
            data = json.load(f)
            data.append({
                "title": vacancy.title,
                "link": vacancy.link,
                "salary": vacancy.salary,
                "description": vacancy.description
            })
        with open(self.file_path, "w") as f:
            json.dump(data, f)

    def get_vacancies_by_criteria(self, criteria):
        with open(self.file_path, "r") as f:
            data = json.load(f)
            return [Vacancy(v["title"], v["link"], v["salary"], v["description"]) for v in data if criteria in v["description"]]

    def delete_vacancy(self, vacancy):
        with open(self.file_path, "r") as f:
            data = json.load(f)
            data = [v for v in data if v["link"] != vacancy.link]
        with open(self.file_path, "w") as f:
            json.dump(data, f)


