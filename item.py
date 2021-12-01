import mysql.connector
import sys

from mysql_database import connect_database


#items:
#	-view all items
#	-add item(s)
#	-remove item(s)


class items(object):

    def __init__(item, item_name, item_price, item_quantity):
        item.item_name = item_name
        item.item_price = item_price
        item.item_quantity = item_quantity
    
    def view_all():
        connection, cursor = connect_database()

        query = "SELECT * FROM items"

        data = (item.item_name, item.item_price, item.item_quantity)


        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()