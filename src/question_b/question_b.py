#write functions here, don't add input('') statements here!

def create_multiplication_table(i,j):

    mult_list = []
    x = 0

    for x in range(1,j+1):
        row_list = []
        for y in range(1,i+1):
            row_list.append(x*y)
        mult_list.append(row_list)

    return mult_list

def display_multiplication_table(list_parameter):


    grid = ""

    for x in list_parameter:
        grid = grid + "\n"
        for y in x:
            grid = grid + str(y) + " "

    return grid

