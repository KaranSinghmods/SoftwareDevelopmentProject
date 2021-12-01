from user import *
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
    print("\nLogging in...")

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
