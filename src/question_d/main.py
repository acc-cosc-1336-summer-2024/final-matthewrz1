#add import

from question_d import Stock
from question_d import stock_purchase_history

def menu():

    print("Question d menu, please choose an option below")
    print("1-Display stock purchase history")
    print("2-Exit")

    selection = int(input("Please choose a menu item above: "))
    x = True
    Ask_Exit = "N"

    if selection == 1:

        while x == True:
            print("The stock purchase table is:", "\n")
            stock_purchase_history()
            Ask_Exit = input("Would you like to exit? Y or N: ").upper()
            print("\n")
            if Ask_Exit == "Y":
                print("You have exit the menu")
                exit()
            elif Ask_Exit == "N":
                print("Staying in p distance matrix menu option")
                #print("The stock purchase table is: ", "\n")
                #stock_purchase_history()

    elif selection == 2:

        while x == True:
            Ask_Exit = input("Would you like to continue? Y or N: ").upper()
            if Ask_Exit == "N":
                print("You have exit the menu")
                exit()
            elif Ask_Exit == "Y":
                menu()
    
    else:
        print("Menu option not recognized, please input a number from 1 to 2")
        menu()

menu()
