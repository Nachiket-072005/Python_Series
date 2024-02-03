# Search for a number x in this tuple using loop : 

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36

idx = 0
for val in tup:
    if(val == x) :
        print("Found at idx", idx)
    idx += 1
