#write functions here, don't add input('') statements here!

def lowest_num(num_list):

    num_list.sort()

    return num_list[0]


def highest_num(num_list):

    num_list.sort()

    return num_list[len(num_list)-1]


def total(num_list):

    total = 0

    for x in num_list:
        total += x

    return total


def average(num_list):

    total = 0

    for x in num_list:
        total += x

    average = total/len(num_list)

    return average






