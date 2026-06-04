import pymysql

def db_connect():
    connection = None
    try:
        connection = pymysql.connect(user = 'root', password = 'root1', port = 3306, database = 'ananya_db', charset = 'utf8', host = 'localhost')
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

connection = db_connect()
db_disconnect(connection)