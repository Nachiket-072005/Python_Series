# Recursive Approach

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
number = int(input("Enter the number you want to see the factorial of: "))

# print(fact(number))

# Normal Way

fact = 1

for i in range(1, number+1):
    fact *= i

print(fact)