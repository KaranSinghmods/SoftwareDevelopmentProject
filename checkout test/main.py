from user import *
from item import *
from shopping_cart import *
import mysql.connector
import sys

# Main Driver
if __name__ == '__main__':

    # Connecting to the database
    connection, cursor = connect_database()

    # Entering Before-Login Loop
    # Correct inputs: 'Login', 'Create Account', 'Exit'
    print("Welcome to the Software Development E-Commerce Store\n")
    while True:
        print("Would you like to login or create a new account?")
        response = input("(Login/Create Account/Exit): ")
        if (response != "Login") and (response != "Create Account") and (response != "Exit"):
            print("Invalid response\n")
            continue
        else:
            break

    # Login to your account
    if response == "Login":
        print("Logging In...\n")

        while 1:
            username = input("Username: ")
            password = input("Password: ")

            my_account = User(username, password)
            if my_account.login():
                break
            print("Incorrect username/password\n")

    # Create a New Account
    elif response == "Create Account":
        print("Creating New Account...\n")

        while 1:
            username = input("Please choose a username: ")
            # checks to see if username already exists

            cursor.execute("SELECT username FROM user")
            result = cursor.fetchall()

            username_exist = False
            for x in result:
                if x[0] == username:
                    print("ERROR - username already exists\n")
                    username_exist = True

            if not username_exist:
                break

        password = input("Password: ")
        # Default shipping/billing address
        shipping_address = input("Shipping Address: ")
        billing_address = input("Billing Address: ")
        payment_info = input("Payment Info: ")

        my_account = User(username, password)
        my_account.create_account(shipping_address, billing_address, payment_info)
        my_account.login()

        # FIXME - Deletes the account to prevent spam account (for testing)
        # my_account.delete_account()

    elif response == "Exit":
        print("Exiting the e-commerce store...")
        sys.exit()

    # After-Login
    # my_account has the current user
    print("\nLogging in...\n")

    while 1:
        print("Commands: ")

        print("\tView Item Inventory")
        print("\tDelete Account")

        print("\tAdd to Cart")
        print("\tRemove from Cart")
        print("\tView Cart")

        print("\tCheckout")
        print("\tLogout")
        print()

        test_input = input("Enter a command: ")

        if test_input == "View Item Inventory":
            show = Item(username)
            show.view_all()

        elif test_input == "Delete Account":
            my_account.delete_account()
            print("Deleting Account")
            break

        elif test_input == "Add to Cart":
            item_name = input("What item would you like to add: ")
            # check if the item exists - item class
            item_quantity = input("What quantity would you like: ")
            # checks if the item quantity is available - item class

            my_cart = Shopping_Cart(username)
            my_cart.add_to_cart(item_name, item_quantity)

        elif test_input == "Remove from Cart":
            item_name = input("What item would you like to remove: ")

            my_cart = Shopping_Cart(username)
            my_cart.remove_from_cart(item_name)

        elif test_input == "View Cart":
            my_cart = Shopping_Cart(username)
            my_cart.view_cart()

        elif test_input == "Checkout":
            checkout = checkout(username)
            if checkout.confirmorder():

                my_item = Item(username)
                my_item.edit_item_count()

                connection, cursor = connect_database()

                query("DELETE FROM shopping_cart WHERE username=%s")
                data = (self.username,)

                cursor.execute(query, data)
                connection.commit()

                cursor.close()
                connection.close()

            else:
                connection, cursor = connect_database()

                query("DELETE FROM shopping_cart WHERE username=%s")
                data = (self.username,)

                cursor.execute(query, data)
                connection.commit()

                cursor.close()
                connection.close()

            # Confirm

        elif test_input == "Logout":
            print("Logging out...")
            break

        '''
        elif test_input == "edit inventory":
            edit_count = Item(username)
            edit_count.edit_item_count()
        '''

        '''  
        print("Show a list of items available w/ current availability")
        # available should only change when the item has been checked out,
        # not when it has been added to the user's shopping cart
        print("Example:")
        print("\tItem: 1 \tCount: 13 \tPrice: $11.99")
        print("\tItem: 2 \tCount: 9 \tPrice: $6.99")
        print("\tItem: n \tCount: n \tPrice: $-.--")

        print("Options:")
        print("\tAdd item to Shopping Cart")
        print("\tView Shopping Cart")
        print("\tRemove item from Shopping Cart")
        print("\tCheck-out Shopping Cart")
        # Option to either use default shipping/billing or change in database
        # Alters item count upon success
        # Displays total cost

        print("\tView Order History")
        # Computes each order price w/ count to display total cost per order

        print("\tView Items Available")
        # Displays Item list again

        print("\tLogout")
        # Either exits the program or goes back into Before-Login Loop
        # Exits for now
        '''


    '''
    query = ("SELECT * FROM Shopping_Cart WHERE username=%s")
    data = (self.username, )

    cursor.execute(query, data)
    result = cursor.fetchall()

    total_value = 0

    for x in result:
        query2 = "SELECT item_price FROM Item WHERE item_id=%s"
        data2 = x[0]
        cursor.execute(query2, data2)
        result2 = cursor.fetchall()

        for x2 in result2:
            item_count = x[2] # store item count
            item_price = x2[2] # store item price

            temp_value = item_count * item_price

        total_value += temp_value

    print("Your total is: ", total_value)

    cursor.close()
    connection.close()
    '''