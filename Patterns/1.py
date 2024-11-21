## Pattern No - 1

def pattern1(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()

# pattern1(5)

## Pattern No - 2

def pattern2(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print("*", end=" ")
        print()

# pattern2(5)

## Pattern No - 3

def pattern3(n):
    for i in range(1, n+1):
        for j in range(5, i-1, -1):
            print("*", end="")
        print()

# pattern3(5)

## Pattern No - 4

def pattern4(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()

# pattern4(5)

## Pattern No - 5

def pattern5(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end="")
        print()

def pattern6(n):
    for i in range(1, n+1):
        for j in range(4, i-1, -1):
            print("*", end="")
        print()

# pattern5(5)
# pattern6(4)

## Pattern No - 7

def pattern7(n):
    for i in range(1, 2*n):
        if i > n:
            C = 2*n - i
        else:
            C = i
        for j in range(1, C+1):
            print("*", end="")
        print()
    
pattern7(10)