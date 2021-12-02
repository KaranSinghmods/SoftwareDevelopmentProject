import mysql.connector
import sys

from mysql_database import connect_database

class Shopping_Cart:
    def __init__(self, username):
        self.username = username

    def add_to_cart(self, item_name, item_quantity):
        print("Add to cart\n")
        connection, cursor = connect_database()

        cursor.execute("SELECT * FROM Item")
        result = cursor.fetchall()
        for x in result:
            if x[1] == item_name:
                print("x[0]:", x[0])
                print("x[1]:", x[1])
                item_id = x[0]

        query = "INSERT INTO Shopping_Cart (username, item_id, item_count) " \
                "VALUES (%s, %s, %s)"
        data = (self.username, item_id, item_quantity)

        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

    def remove_from_cart(self, item_name):
        print("Remove to cart\n")
        connection, cursor = connect_database()

        cursor.execute("SELECT * FROM Item")
        result = cursor.fetchall()
        for x in result:
            if x[1] == item_name:
                print("x[0]:", x[0])
                print("x[1]:", x[1])
                item_id = x[0]

        cursor.execute("SELECT * FROM Shopping_Cart")
        result = cursor.fetchall()
        #for x in result:

        query = "DELETE FROM Shopping_Cart WHERE item_id=%s AND username=%s"
        data = (item_id, self.username)

        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

        '''
        if x[0] == self.username:
            if x[1] == item_id:
                query = "DELETE FROM Shopping_Cart WHERE item_id=%s"
                data = item_id

                cursor.execute(query, data)
                connection.commit()
                cursor.close()
                connection.close()
        '''

    def view_cart(self):
        connection, cursor = connect_database()

        cursor.execute("SELECT * FROM Shopping_Cart")
        result = cursor.fetchall()
        for x in result:
            if x[0] == self.username:
                print(x)

        cursor.close()
        connection.close()

    # def checkout(self):
