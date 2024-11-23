import numpy as np

array = np.array([
    ['A', 'B', 'C'],
    ['C', 'D', 'C'],
    ['E', 'F', 'C']
])

count_C = np.sum(array == 'C')

print(f"Number of 'C' element in the array: {count_C}")