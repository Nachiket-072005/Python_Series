# Seed Value
F0 = 0
F1 = 1

numberRange = int(input("Enter the range of the number you want to see: "))

# Normal Way
print(f"{F0} {F1}", end=" ")
count = numberRange - 2

while count > 0:
    FN = F0 + F1
    print(FN, end=" ")
    F0 = F1
    F1 = FN
    count -= 1

print()

# Recursive Way

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
for i in range(numberRange):
    print(fib(i), end=" ")

print()