#add import

import question_b

def menu():

    print("question b menu, please choose an option below")
    print("1-create multiplication table")
    print("2-exit")

    selection = int(input("Please choose a menu item above: "))
    x = True
    Ask_Exit = "N"

    if selection == 1:

        j = int(input("You have chosen create multiplication table, enter how many rows the table will have: "))
        i = int(input("You have chosen create multiplication table, enter how many columns the table will have: "))

        while x == True:
            if i > 0 and j > 0:

                display = question_b.create_multiplication_table(i,j)
                print("multiplication table is: ", question_b.display_multiplication_table(display))
                Ask_Exit = input("Would you like to exit? Y or N: ").upper()
                if Ask_Exit == "Y":
                    print("You have exit the menu")
                    exit()
                elif Ask_Exit == "N":
                    print("Staying in multiplication menu option")
                    j = int(input("You have chosen to stay in create multiplication table, enter how many rows the table will have: "))
                    i = int(input("You have chosen create multiplication table, enter how many columns the table will have: "))

            elif i < 1 or j < 1:
                j = int(input("Enter more rows than 0, enter how many rows the table will have: "))
                i = int(input("Enter more columns than 0, enter how many columns the table will have: "))
    
    elif selection == 2:

        while x == True:
            Ask_Exit = input("Would you like to continue? Y or N: ").upper()
            if Ask_Exit == "N":
                print("You have exit the menu")
                exit()
            elif Ask_Exit == "Y":
                menu()


menu()
