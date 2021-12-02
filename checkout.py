import mysql.connector
import sys

from mysql_database import connect_database
from shopping_cart import *

class Checkout:
    # def __init__(self):

    def __init__(self, username):
        self.username = username
        # self.totalcost = totalcost
    '''
    def verifypayment(self):
        connection, cursor = connect_database()
        cursor.execute("SELECT payment_info FROM User")
        result = cursor.fetchall()

        print("Your payment info is labeled as being ", result)
        ans = input("Is this correct (Y/n)")
        while 1:
            if (ans != "Y") and (ans != "y") and (ans != "N") and (ans != "n"):
                print("That was not a valid response")
                ans = input("Is your payment info correct? (Y/n)")
                continue
            else:
                break

        if (ans == "Y") or (ans == "y"):
            return

        if (ans == "N") or (ans == "n"):
            # delete old payment info from database

            data = input("What is your payment info?")

            query = "INSERT INTO User(payment_info)" \
                    "VALUES (%s)"

            curser.execute(query, data)
            connection.commit()
            cursor.close()
            connection.close()

            print("Your payment info has been updated")

    def verifyshipping(self):
        connection, cursor = connect_database()
        cursor.execute("SELECT shipping_address FROM User")
        result = cursor.fetchall()

        print("Your shipping address is labeled as being ", result)
        ans = input("Is this correct (Y/n)")
        while 1:
            if(ans != "Y") and (ans != "y") and (ans != "N") and (ans != "n"):
                print("That was not a valid response")
                ans = input("Is your shipping address correct? (Y/n)")
                continue
            else:
                break

        if (ans == "Y") or (ans == "y"):
            return

        if (ans == "N") or (ans == "n"):
            new_ship = input("What is yo")
            query1 = "UPDATE "

            cursor.execute(query1)
            connection.commit()

            data = input("What is your shipping address?")

            query = "INSERT INTO User(shipping_address) VALUES (%s)"

            curser.execute(query, data)
            connection.commit()
            cursor.close()
            connection.close()

            print("Your shipping address has been updated")
    '''

    def confirmorder(self):
        print("Your shopping cart is listed as having these items in it:")

        connection, cursor = connect_database()
        # connection2, cursor2 = connect_database()

        my_cart = Shopping_Cart(self.username)
        my_cart.view_cart()

        query = "SELECT * FROM Shopping_Cart WHERE username=%s"
        data = (self.username, )

        cursor.execute(query, data)
        result = cursor.fetchall()

        # temp
        #cursor.close()
        #connection.close()

        totalValue = 0

        for x in result:
            query2 = "SELECT item_price FROM Item WHERE item_id=%s"
            data2 = (x[1], )

            cursor.execute(query2, data2)
            result2 = cursor.fetchall()

            for testx2 in result2:
                print("c1", x[2])
                item_count = x[2]
                print("t1", testx2[0])
                item_price = testx2[0]

                temp_value = item_count * item_price

            totalValue += temp_value

        cursor.close()
        connection.close()

        print("The total cost of these items is: $" + str(totalValue))

        ans = input("Is your order correct? (Y/n)")

        while 1:
            if(ans != "Y") and (ans != "y") and (ans != "N") and (ans != "n"):
                print("That was not a valid response")
                ans = input("Is your order correct? (Y/n)")
                continue
            else:
                break

        if(ans == "Y") or (ans == "y"):
            return True

        if(ans == "N") or (ans == "n"):
            # clear the shopping cart
            return False

    def add_to_order(self):
        connection, cursor = connect_database()

        query = "SELECT * FROM Shopping_Cart WHERE username=%s"
        data = (self.username, )

        cursor.execute(query, data)
        result = cursor.fetchall()

        for x in result:
            query2 = "INSERT INTO order_history (username, order, item_id, item_count) " \
                        "VALUES (%s, %s, %s, %s)"
            data2 = (x[0], 0, x[1], x[2])

            cursor.execute(query2, data2)
            connection.commit()
            cursor.close()
            connection.close()

'''
 #   def cancel(self):
 #       ans  = input("Would you like to cancel")
 #       while 1:
 #           if (ans != "Y") and (ans != "y") and (ans != "N") and (ans != "n"):
 #               print("That was not a valid response")
 #               ans = input("Is your order correct? (Y/n)")
 #               continue
 #           else:
 #               break

 #       if (ans == "Y") or (ans == "y"):
 #           return

 #       if (ans == "N") or (ans == "n"):
 #           return
'''