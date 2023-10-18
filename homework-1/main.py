"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
with open('C:\\Users\\wwwru\\pythonProject3\\postgres-homeworks\\homework-1\\north_data\\employees_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)
    print(data)
conn = psycopg2.connect(host='localhost', database='north',user='postgres', password='656565Asd12')
try:
    with conn:
        with conn.cursor() as cur:
            for i in data:
                cur.execute('INSERT INTO employees VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT (employee_id) DO NOTHING',(i['employee_id'], i['first_name'], i['last_name'],i["title"],i["birth_date"],i['notes']))
                conn.commit()
            cur.execute("SELECT * FROM employees")
            rows = cur.fetchall()
            for row in rows:
                print(row)
finally:
    conn.close()