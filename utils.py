def filter_vacancies(*vacancies, filter_words):
    filtered_vacancies = []
    for v in vacancies:
        if v is None:
            continue
        for w in filter_words:
            if v.description is not None and w in v.description:
                filtered_vacancies.append(v)
                break
    return filtered_vacancies

def sort_vacancies(vacancies):
    return sorted(vacancies)

def get_top_vacancies(vacancies, n):
    return vacancies[:n]

def print_vacancies(vacancies):
    for v in vacancies:
        print(v.title, v.link, v.salary, v.description)