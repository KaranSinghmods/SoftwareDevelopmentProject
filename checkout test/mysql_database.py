import mysql.connector
import sys

def connect_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            # Change password and database below
            password="",
            database="swd_project"
        )
        print("Successful connection.")
    except:
        print("Failed connection.")
        sys.exit()

    cursor = connection.cursor()
    return connection, cursor
