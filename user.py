import mysql.connector
import sys

from mysql_database import connect_database

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_account(self, shipping_address, billing_address, payment_info):
        # print("Creating the account,", self.username)

        connection, cursor = connect_database()

        query = "INSERT INTO User (username, password, shipping_address, billing_address, payment_info) " \
                "VALUES (%s, %s, %s, %s, %s)"
        data = (self.username, self.password, shipping_address, billing_address, payment_info)

        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

    def login(self):
        # print("Logging in..", self.username)

        connection, cursor = connect_database()

        cursor.execute("SELECT username, password FROM User")
        result = cursor.fetchall()
        for x in result:
            if x[0] == self.username and x[1] == self.password:
                cursor.close()
                connection.close()
                return True
        cursor.close()
        connection.close()
        return False

    def logout(self):
        # No functionality for now
        # Maybe allows the user to logout so they can log-in again w/ a different account
        print("Logging out..", self.username)

    def delete_account(self):
        # Deletes the current account
        print("Deleting..", self.username)

        connection, cursor = connect_database()

        query = "DELETE FROM User WHERE username =%s"
        data = (self.username, )

        cursor.execute(query, data)
        connection.commit()

        query = "DELETE FROM Shopping_Cart WHERE username =%s"
        data = (self.username, )

        cursor.execute(query, data)
        connection.commit()

        query = "DELETE FROM Order_History WHERE username =%s"
        data = (self.username, )

        cursor.execute(query, data)
        connection.commit()

        cursor.close()
        connection.close()

        print("Deleted.")
