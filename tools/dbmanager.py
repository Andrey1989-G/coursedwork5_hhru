# обрабатывает данные в БД.
from services.dbconnect import conn
from data.data_with_employer import list_with_employer
from services.input_error import Input_error


class DBManager():
    # добавить метод проверки по айди в бд
    """подключается к БД PostgreSQL. Имеет следующие функции:

    get_companies_and_vacancies_count() — получает список всех компаний
    и количество вакансий у каждой компании.

    get_all_vacancies()— получает список всех вакансий с указанием
    названия компании, названия вакансии и зарплаты и ссылки на вакансию.

    get_avg_salary() — получает среднюю зарплату по вакансиям.

    get_vacancies_with_higher_salary() — получает список всех вакансий,
    у которых зарплата выше средней по всем вакансиям.

    get_vacancies_with_keyword() — получает список всех вакансий,
    в названии которых содержатся переданные в метод слова, например python.
    """

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании."""
        # select distinct name_employer from vacancies
        # select count(name_employer) from vacancies where name_employer = 'Яндекс'
        try:
            with conn:
                with conn.cursor() as cur:
                    for employer in list_with_employer:
                        cur.execute(f"select count(name_employer) from vacancies where name_employer={employer}")
                        rows = cur.fetchall()
                        for row in rows:
                            print(row)
        finally:
            # закрытие соединения
            conn.close()


    def get_all_vacancies(self):
        """
        получает список всех вакансий с указанием
        названия компании, названия вакансии и зарплаты и ссылки на вакансию
        """
        pass

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""
        pass

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        pass

    def get_vacancies_with_keyword(self):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        pass








