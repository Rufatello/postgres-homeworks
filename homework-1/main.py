"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

def load_file(path_file):
    
    '''функция для чтения файла, ему присваиваем переменные, которые написанные ниже'''
    
    with open(path_file, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        return data
        
'''пути для передачи значения в функцию load_file'''

employees_data = load_file('/home/geydarovr/Загрузки/pythonProject/postgres-homeworks/homework-1/north_data/employees_data.csv')
orders_data = load_file('/home/geydarovr/Загрузки/pythonProject/postgres-homeworks/homework-1/north_data/orders_data.csv')
customers_data = load_file('/home/geydarovr/Загрузки/pythonProject/postgres-homeworks/homework-1/north_data/customers_data.csv')
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')
try:
    with conn:
        with conn.cursor() as cur:
            '''создаем 3 цикла для заполнения таблиц'''
            for cus in customers_data:
                cur.execute('INSERT INTO customers VALUES (%s,%s,%s) ON CONFLICT (customer_id) DO NOTHING',(cus['customer_id'], cus['company_name'], cus['contact_name']))
                conn.commit

            cur.execute("SELECT * FROM customers")
            rows = cur.fetchall()
            
            '''вывод таблицы'''
            
            for row in rows:
                print(row)

            for ord in orders_data:
                cur.execute('INSERT INTO orders VALUES (%s,%s,%s,%s,%s) ON CONFLICT (order_id) DO NOTHING', (ord['order_id'], ord['customer_id'], ord['employee_id'], ord['order_date'], ord['ship_city']))
                conn.commit
            cur.execute('SELECT*FROM orders')
            rows = cur.fetchall()
            
            '''вывод таблицы'''
            
            for row in rows:
                print(row)

            for emp in employees_data:
                cur.execute('INSERT INTO employees VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT (employee_id) DO NOTHING', (emp['employee_id'], emp['first_name'], emp['last_name'], emp["title"], emp["birth_date"], emp['notes']))
                conn.commit
            cur.execute("SELECT * FROM employees")
            rows = cur.fetchall()
            
            '''вывод таблицы'''
            
            for row in rows:
                print(row)
finally:
    conn.close()
    #Второй вариант закоментирован

"""Скрипт для заполнения данными таблиц в БД Postgres."""
# import psycopg2
# import csv
# 
# def load_file(path_file):
#     with open(path_file, 'r') as file:
#         reader = csv.DictReader(file)
#         data = list(reader)
#         return data
# employees_data = load_file('/home/geydarovr/Загрузки/pythonProject/postgres-homeworks/homework-1/north_data/employees_data.csv')
# orders_data = load_file('/home/geydarovr/Загрузки/pythonProject/postgres-homeworks/homework-1/north_data/orders_data.csv')
# customers_data = load_file('/home/geydarovr/Загрузки/pythonProject/postgres-homeworks/homework-1/north_data/customers_data.csv')
# conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')
# try:
#     with conn:
#         with conn.cursor() as cur:
#             for cus, emp, ort in zip(customers_data, employees_data, orders_data):
#                 cur.execute('INSERT INTO customers VALUES (%s,%s,%s) ON CONFLICT (customer_id) DO NOTHING',(cus['customer_id'], cus['company_name'], cus['contact_name']))
#                 cur.execute('INSERT INTO employees VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT (employee_id) DO NOTHING', (emp['employee_id'], emp['first_name'], emp['last_name'], emp["title"], emp["birth_date"], emp['notes']))
#                 cur.execute('INSERT INTO orders VALUES (%s,%s,%s,%s,%s) ON CONFLICT (order_id) DO NOTHING', (ort['order_id'], ort['customer_id'], ort['employee_id'], ort['order_date'], ort['ship_city']))
#                 conn.commit
# 
#             cur.execute("SELECT * FROM customers")
#             rows = cur.fetchall()
#             cur.execute('SELECT*FROM orders')
#             rows_1 = cur.fetchall()
#             cur.execute("SELECT * FROM employees")
#             rows_2 = cur.fetchall()
#             for row in rows:
#                 print(row)
#             for row_1 in rows_1:
#                 print(row_1)
#             for row_2 in rows_2:
#                 print(row_2)
# 
# finally:
#     conn.close()
