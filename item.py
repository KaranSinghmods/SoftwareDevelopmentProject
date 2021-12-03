import mysql.connector
import sys

from mysql_database import connect_database

'''
class Item:
    def __init__(self):

    def add_item(self):
        # connection, cursor = connect_database()

        # cursor.execute("SELECT

    def remove_item(self):

    def show_all_items(self):
'''

class Item:

    def __init__(self, username):
        self.username = username

    def view_all(self):
        connection, cursor = connect_database()

        cursor.execute("SELECT * FROM item")
        result = cursor.fetchall()

        print("\nPrice:\tQuantity:\tBook Title:")
        for x in result:
            print(x[2], "\t", x[3], "\t\t", x[1])
        print()

        cursor.close()
        connection.close()

    def edit_item_count(self):
        # print("Edit Item Count")
        connection, cursor = connect_database()

        query = "SELECT * FROM Shopping_Cart WHERE username=%s"
        data = (self.username, )

        cursor.execute(query, data)
        result = cursor.fetchall()

        for x in result:
            # print(x[1])
            query2 = "UPDATE Item SET item_quantity=item_quantity-%s WHERE item_id=%s"
            data2 = (x[2], x[1])
            cursor.execute(query2, data2)
            connection.commit()

        cursor.close()
        connection.close()

    def restock_item(self):
        print("Secret Item Function")
        connection, cursor = connect_database()

        cursor.execute("SELECT * FROM Item")
        result = cursor.fetchall()

        for x in result:
            query = "UPDATE Item SET item_quantity=%s"
            data = (100, )
            cursor.execute(query, data)
            connection.commit()

        cursor.close()
        connection.close()

