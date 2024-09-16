import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='mysql',
        user='admin',
        password='saberpro2024',
        database='saberproDB'
    )
    return connection
