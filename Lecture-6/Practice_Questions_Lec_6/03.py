# WAF to find the factorial of n. (n is the parameter.)

def find_Fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    
    print(fact)

find_Fact(7)