# First, We will create empty set then use sets of methods

collection = set()

collection.add(1)
collection.add(2)
collection.add(3)
collection.add(1)
collection.add(5)
collection.add((7, 8, 9))
collection.add("Hello Ji")

# collection.remove(5)
# collection.remove(3)
# collection.clear()
print(collection)
print(collection.pop())
print(collection)
print(len(collection))

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2)) #{1, 2, 3, 4}
print(set1.intersection(set2)) #{2, 3}