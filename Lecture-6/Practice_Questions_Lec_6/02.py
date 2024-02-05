# WAF to print the elements of a list in a single line.(list is the parameter.)

def print_List(list):
    for el in list:
        print(el, end=" ")

list = [1, 2, 3, 4, 5]
print_List(list)