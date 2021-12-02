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
    # def __init__(self, item_name, item_price, item_quantity):
        # self.item_name = item_name
        # self.item_price = item_price
        # self.item_quantity = item_quantity

    def __init__(self, username):
        self.username = username

    def view_all(self):
        connection, cursor = connect_database()

        cursor.execute("SELECT * FROM item")
        result = cursor.fetchall()
        for x in result:
            print(x)

        cursor.close()
        connection.close()

    def edit_item_count(self):
        print("Edit Item Count")
        connection, cursor = connect_database()

        # query = "SELECT * FROM Shopping_Cart"

        # FIXME - Hard-coded 'u1' username
        # query = "SELECT * FROM Shopping_Cart WHERE username='u1'"

        query = "SELECT * FROM Shopping_Cart WHERE username=%s"
        data = (self.username, )
        # print(self.username)

        cursor.execute(query, data)
        # cursor.execute(query)
        result = cursor.fetchall()

        for x in result:
            # print(x[1])
            query2 = "UPDATE Item SET item_quantity=item_quantity-%s WHERE item_id=%s"
            data2 = (x[2], x[1])
            cursor.execute(query2, data2)
            connection.commit()

        cursor.close()
        connection.close()

        # query = "UPDATE Item SET item_quantity=%s WHERE item_id=&

        # query = "UPDATE Item.item_quantity SET item.item_quantity - Shopping_Cart.item_count " \
        #         "WHERE Shopping_Cart.item_id = Item.item_id"

        # cursor.execute(query)
        # cursor.execute("UPDATE Item.item_quantity ")


