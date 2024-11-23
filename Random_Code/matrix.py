import numpy as np

def generate_matrix(x, y):
    array = np.zeros((x,y), dtype=int)

    for i in range(x):
        for j in range(y):
            array[i][j] = i * j
        
    return array

x = int(input("Enter the number of rows: "))
y = int(input("Enter the number of columns: "))

res = generate_matrix(x, y)
print("2D Array: ")
print(res)
