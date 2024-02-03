# WAP to find the factorial of first n numbers.(using for)
N = int(input("Enter the value of N : "))

fact = 1
for i in range(N, 0, -1):
    fact *= i

print("Factorial of", N, "is", fact)