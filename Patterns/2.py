# Some of different patterns

# 1. Pattern 1

def pattern1(n):
    for i in range(1, 2*n):
        if i > n:
            C = 2*n - i
        else:
            C = i
        # Spaces
        for k in range(1, n-C+1):
            print(end=" ")
        for j in range(1, C+1):
            print("*", end=" ")
        print()

# pattern1(5)

# 2. Pattern 2

def pattern2(n):
   for row in range(1, n+1):
        print(" " * (n-row)*2, end=" ")
        for col in range(row, 0, -1):
            print(col, end=" ")
        for col in range(2, row+1):
            print(col, end=" ")
        print()

pattern2(5)