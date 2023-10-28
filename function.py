from tools.dbloader import DBLoader
from tools.dbmanager import DBManager
import time
from data.data_with_employer import list_with_employer

def main_theme():
    # print('загрузка данных...')
    # time.sleep(0.4)
    # print('.')
    # time.sleep(0.4)
    # print('..')
    # time.sleep(0.4)
    # print('...')
    # time.sleep(0.4)
    # print('....')
    # time.sleep(0.7)
    # print('загрузка завершена')
    # s = DBLoader()
    # for employer in list_with_employer:
    #     s.data_preparation_and_load_in_db(s.get_vacancies(employer))

    s = DBManager()
    # s.get_companies_and_vacancies_count()
    # s.get_all_vacancies()
    # s.get_avg_salary()
    # s.get_vacancies_with_higher_salary()
    s.get_vacancies_with_keyword('способ')




s = DBLoader()

# s.big_red_button('vacancies')

main_theme()

# s = DBManager()

# s.get_companies_and_vacancies_count()