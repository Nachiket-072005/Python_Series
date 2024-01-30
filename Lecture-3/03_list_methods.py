#List Methods
list = [2, 1, 3]
# List will return none value
list.append(4)
print(list)

list.insert(1, 5)
print(list)

list.reverse()
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list) 

ch = ['A', 'D', 'E', 'F', 'B', 'C']
ch.sort()
print(ch)

fruits = ["banana", "litchi", "apple"]
fruits.sort()
fruits.sort(reverse=True)
print(fruits)


list = [2, 1, 3, 1]
list.remove(1) #It will remove first occurrance of the element
print(list)
list.pop(1)
print(list)