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

def insert_row():
    query = 'insert into employees(id, name, designation, salary, phone) values(23, "Ananya", "Software Engineer", 75000, 9876543210)'
    try:
        connection = dbc.db_connect()
        cursor = connection.cursor()
        result = cursor.execute(query)
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

