import MySQLdb

database = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='7328'  
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS elderco")

print("All Done!")