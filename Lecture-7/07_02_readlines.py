f = open("demo.txt", "r")
line1 = f.readlines()
print(line1)
line2 = f.readline()
print(line2)
print(type(line1))
print(type(line2))
f.close()