import pymysql
import db_connect2 as dbc

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

create_db()
create_table()





        #query = 'create table if not exists employees(id int primary key auto_increment, name varchar(255) not null, age int, department varchar(255), designation varchar(255), salary float, commission float default 0, years_of_experience tinyint, phone bigint unique)'