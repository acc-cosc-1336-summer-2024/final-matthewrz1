#add import

import question_c

def menu():

    print("question c menu, please choose an option below: ")
    print("1-Number stats")
    print("2-Exit")

    selection = int(input("Please choose a menu item above: "))

    x = True
    Ask_Exit = "N"

    if selection == 1:

        print("Please enter 5 numbers, press enter after each number")
        q_count = 0
        num_list = []

        while q_count < 5:
            try:
                for i in range(q_count, 5):
                    number = int(input("Enter a number: "))
                    num_list.append(number)
                    q_count += 1
            except ValueError:
                print("Did not enter a number, enter a number:")
        
        while x == True:
            if len(num_list) > 0:
                print("Your list is: ", num_list)
                lowest_num = question_c.lowest_num(num_list)
                highest_num = question_c.highest_num(num_list)
                total_num = question_c.total(num_list)
                average_num = question_c.average(num_list)

                print("Lowest number is: ", lowest_num)
                print("Highest number is: ", highest_num)
                print("Total is:", total_num)
                print("Average is: ", average_num)
                Ask_Exit = input("Would you like to exit? Y or N: ").upper()

                if Ask_Exit == "Y":
                    print("You have exit the menu")
                    exit()

                elif Ask_Exit == "N":
                    print("Staying in number menu")
                    print("Please enter 5 numbers, press enter after each number")
                    q_count = 0
                    num_list = []

                    while q_count < 5:
                        try:
                            for i in range(q_count, 5):
                                number = int(input("Enter a number: "))
                                num_list.append(number)
                                q_count += 1
                        except ValueError:
                            print("Did not enter a number, enter a number:")
            
            elif len(num_list) < 1:
                print("Please enter 5 numbers, press enter after each number")
                q_count = 0
                num_list = []

                while q_count < 5:
                    try:
                        for i in range(q_count, 5):
                            number = int(input("Enter a number: "))
                            num_list.append(number)
                            q_count += 1
                    except ValueError:
                        print("Did not enter a number, enter a number:")
    
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




