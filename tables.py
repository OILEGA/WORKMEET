import mysql.connector

#Establish connection
connection = mysql.connector.connect(
        host= 'localhost',
        user= 'root',
        passwd= 'Dilegs',
        database= 'workmeet_reg'
        )

cursor= connection.cursor()

cursor.execute('SHOW TABLES')

tables= cursor.fetchall()
for table in tables:
    print(table[0])

cursor.close()
connection.close()

