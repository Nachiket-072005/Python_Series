# Print multiplication table of a number of n :

num = int(input("Enter the number : "))

for i in range(1, 11):
    print(num, "*", i, "=", num * i)