import pymysql

connection = pymysql.connect(user = 'root', password = 'root', port = 3306, database = 'ananya_db', charset = 'utf8', host = 'localhost')

print('DB connected')
connection.close()

print('DB disconnected')
