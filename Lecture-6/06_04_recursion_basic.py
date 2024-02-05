# print n to 1 backwards
# recursive function
def show(n):
    if(n == 0): # Base Case 
        return
    print(n)
    show(n-1)


show(10)