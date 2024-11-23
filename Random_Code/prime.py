import math

num = int(input("Enter the number you wanna check if it is a prime no or not? "))

if num == 2:
    print("No is prime")
    exit()

def is_Prime(n):
    sqrt = int(math.sqrt(n))
    if n <= 1:
        return False
    else:
        for i in range(2, sqrt+1):
            if n % i == 0:
                return False
        return True
    
if is_Prime(num):
    print("No is prime")
else:
    print("No is not prime")