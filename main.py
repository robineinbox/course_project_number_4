from api import HeadHunterAPI, SuperJobAPI
from utils import filter_vacancies, sort_vacancies, get_top_vacancies, print_vacancies
from vacancy_file import JSONSaver

def get_vacancies(api, search_query):
    return api.get_vacancies(search_query)


hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI(token="v3.r.130652594.27ff989ff274d7c7b7fcefe09326e1f18e40f7c0.cbfac876b3dc96532e1f96c5e417a52ed7c8b18f")

search_query = input("Введите поисковый запрос: ")

hh_vacancies = get_vacancies(hh_api, search_query)
superjob_vacancies = get_vacancies(superjob_api, search_query)

all_vacancies = hh_vacancies + superjob_vacancies

for v in all_vacancies:
    print(v.title, v.url, v.salary)
























# from api import HeadHunterAPI, SuperJobAPI
# from vacancy import Vacancy
# from vacancy_file import JSONSaver
# from utils import filter_vacancies, sort_vacancies, get_top_vacancies, print_vacancies
#
# def user_interaction():
#     hh_api = HeadHunterAPI()
#     superjob_api = SuperJobAPI(token="v3.r.130652594.27ff989ff274d7c7b7fcefe09326e1f18e40f7c0.cbfac876b3dc96532e1f96c5e417a52ed7c8b18f")
#     hh_vacancies = hh_api.get_vacancies("Python")
#     superjob_vacancies = superjob_api.get_vacancies("Python")
#
#     platforms = ["HeadHunter", "SuperJob"]
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words=filter_words)
#
#     if not filtered_vacancies:
#         print("Нет вакансий, соответствующих заданным критериям.")
#         return
#
#     sorted_vacancies = sort_vacancies(filtered_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)
#
#
# if __name__ == "__main__":
#     user_interaction()

