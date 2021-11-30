import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Nickajack7!",
    database = "shop"
    )
mycursor = db.cursor()
