import psycopg2

from password import password

conn = psycopg2.connect(
        host="localhost",
        database="db_hh_ru",
        user="postgres",
        password=password
    )

# class DBConnect():
#     """абстрактный класс для коннекта"""
#     # Подключение к db
#     def __init__(self):
#         self.conn = psycopg2.connect(
#         host="localhost",
#         database="db_hh_ru",
#         user="postgres",
#         password=password
#     )