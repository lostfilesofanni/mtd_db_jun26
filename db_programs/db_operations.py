from encodings import search_function
import re
import sys
import pymysql
import db_connect2 as dbc

def db_connect():
    connection = None
    try:
        connection = pymysql.connect(user = 'root', password = 'root', port = 3306, database = 'ananya_db', charset = 'utf8', host = 'localhost')
        print('DB connected')
    except Exception as e:
        print('DB connection failed')
    return connection

def db_disconnect(connection):
    try:
        connection.close()
        print('DB disconnected')
    except Exception as e:  
        print('DB Disconnection failed')

def create_db():
    query = 'create database ananya_db'
    try:
        connection = dbc.db_connect()
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()
        cursor.close()
        #connection.close()
        dbc.db_disconnect(connection)
        if result == 1:
            print('DB created')
        else:
            print('DB already exists')
    except Exception as e:
        print('Error while creating DB: e', e)


def create_table():
    query = 'create table if not exists employees(id int primary key auto_increment, name varchar(255) not null, designation varchar(255), salary float, phone bigint unique)'
    try:
        connection = dbc.db_connect()
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()
        cursor.close()
        #connection.close()
        dbc.db_disconnect(connection)
        if result == 1:
            print('Table created successfully')
        else:
            print('Table already exists')
    except Exception as e:
        print('Error while creating table: e', e)

def read_employee():
    id = int(input('Enter employee id: '))
    name = input('Enter employee name: ')
    designation = input('Enter employee designation: ')
    salary = float(input('Enter employee salary: '))
    phone = int(input('Enter employee phone: '))
    return(id, name, designation, salary, phone)

def insert_employees():
    id, name, designation, salary, phone = read_employee()
    query = 'insert into employees(id, name, designation, salary, phone) values(%s, %s, %s, %s, %s)'
    try:
        connection = dbc.db_connect()
        cursor = connection.cursor()
        employee = (id, name, designation, salary, phone)
        result = cursor.execute(query, employee)
        connection.commit()
        cursor.close()
        #connection.close()
        dbc.db_disconnect(connection)
        if result == 1:
            print('Row inserted successfully')
        else:
            print('Row insertion failed')
    except Exception as e:
        print('Error while inserting row: e', e)

def update_employee():
    id = int(input('Enter employee id whose salary would be updated: '))
    query = 'update employees set salary=%s where id=%s'
    try:
        connection = dbc.db_connect()
        cursor = connection.cursor()
        salary = float(input('Enter new salary: '))
        result = cursor.execute(query, (salary, id))
        connection.commit()
        cursor.close()
        #connection.close()
        dbc.db_disconnect(connection)
        if result == 1:
            print('Row inserted successfully')
        else:
            print('Row insertion failed')
    except Exception as e:
        print('Error while inserting row: e', e)

def delete_employee():
    id = int(input('Enter id of the employee to be deleted : '))
    query = 'delete from employees where id=%s'
    try:
        connection = dbc.db_connect()
        cursor = connection.cursor()
        result = cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        dbc.db_disconnect(connection)
        if result == 1:
            print(f'Employee with id {id} deleted')
        else:
            print(f'Employee with id {id} not found')
    except Exception as e:
        print('Employee deletion failed', e)

def search_employee():
    id = int(input('Enter employee id to search: '))    
    query = 'select * from employees where id=%s'
    try:
        connection = dbc.db_connect()
        cursor = connection.cursor()
        cursor.execute(query, id)
        row = cursor.fetchone()
        if row:
            print(row)
        else:
            print(f'Employee with id {id} not found')
        cursor.close()
        dbc.db_disconnect(connection)
    except Exception as e:
        print('Employee search failed', e)

def list_employees():
    query = 'select * from employees'
    try:
        connection = dbc.db_connect()
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            print('-' *100)
            print('-%5s %-30s %-15s %-10s %-15s ' % ('ID', 'NAME', 'DESIGNATION', 'SALARY', 'PHONE'))
            print('-' *100)
            for row in rows:
                print('-%5s %-30s %-15s %-10s %-15s ' % row)
            print('-' *100)
            
        else:
            print(f'No Employee Record was Found')
        cursor.close()
        dbc.db_disconnect(connection)
    except Exception as e:
        print('Employee listing failed', e)

def menu(choice):
    match choice:
        case 1:
            insert_employees()
        case 2:
            update_employee()  
        case 3:
            delete_employee()
        case 4:
            search_employee()
        case 5:
            list_employees()
        case 6:
            sys.exit('End of Execution')
        case _:
            print('Invalid Choice')

def run_employee_app():
    while True:
        print('1. Insert Employee')
        print('2. Update Employee Salary')
        print('3. Delete Employee')
        print('4. Search Employee')
        print('5. List Employees')
        print('6. Exit')
        choice = int(input('Enter your choice: '))
        menu(choice)

create_db()
create_table()
run_employee_app()

