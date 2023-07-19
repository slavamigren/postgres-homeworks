import psycopg2
import csv
import pprint


with open('.\\north_data\customers_data.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=',', quotechar='"')
    customers_data = [(i['customer_id'],
                       i['company_name'],
                       i['contact_name']) for i in rows]

with open('.\\north_data\employees_data.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=',', quotechar='"')
    employees_data = [(int(i['employee_id']),
                       i['first_name'],
                       i['last_name'],
                       i['title'],
                       i['birth_date'],
                       i['notes']) for i in rows]

with open('.\\north_data\orders_data.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=',', quotechar='"')
    orders_data = [(int(i['order_id']),
                       i['customer_id'],
                       int(i['employee_id']),
                       i['order_date'],
                       i['ship_city']) for i in rows]



conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="12345"
)

try:
    with conn:
        with conn.cursor() as cursor:
            cursor.executemany("INSERT INTO customers_data VALUES (%s, %s, %s)", customers_data)
            cursor.executemany("INSERT INTO employees_data VALUES (%s, %s, %s, %s, %s, %s)", employees_data)
            cursor.executemany("INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)", orders_data)

finally:
    conn.close()
