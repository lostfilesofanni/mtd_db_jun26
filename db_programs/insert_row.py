import pymysql
import db_connect2 as dbc

def insert_employees():
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

insert_employees()
