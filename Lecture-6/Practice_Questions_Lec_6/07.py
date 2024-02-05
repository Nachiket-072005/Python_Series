# WA a recursive function to print all elements in list.(Hint : use list and index as parameters)

list = [1, 2, 3, 4, 5]

def print_List(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_List(list, idx+1)

print_List(list)

