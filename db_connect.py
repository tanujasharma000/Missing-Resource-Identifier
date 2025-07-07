import mysql.connector

def get_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="ajunat@mysql",
        database="disaster_resources"
    )
    return conn