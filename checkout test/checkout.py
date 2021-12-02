import mysql.connector
import sys

from mysql_database import connect_database

class Checkout:
    # def __init__(self):

    def __init__(self, totalcost, username):
        self.username = username
        self.totalcost = totalcost
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

        my_cart = Shopping_Cart(self.username)
        my_cart.view_cart()

        query("SELECT * FROM Shopping_Cart WHERE username=%s")
        data = (self.username, )

        cursor.execute(query, data)
        result = cursor.fetchall()

        for x in result:
            query2("SELECT item_price FROM item WHERE itemid=%d")
            data2 = x[0]

            cursor.execute(query2, data2)
            result2 = cursor.fetchall()

            for x2 in result2:
                item_count = x[2]
                item_price = x2[2]

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
            #clear the shopping cart
            return False

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