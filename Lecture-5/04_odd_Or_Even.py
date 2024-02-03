# To generate odd numbers
i = 1
while i <= 10:
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1

# To generate even numbers 
i = 1
while i <= 10:
    if(i % 2 != 0):
        i += 1
        continue
    print(i)
    i += 1