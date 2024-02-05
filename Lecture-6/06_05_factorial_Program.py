# to find factorial of n 

def find_Fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * find_Fact(n-1) # This is called recurrence and relation.

n = int(input("Enter the value of n : "))
factorial = find_Fact(n)
print("Factorial of", n,"is",factorial)