# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

dict = {}

m1 = {"phy" : int(input("Enter the marks of phy : "))}
m2 = {"chem" : int(input("Enter the marks of chem : "))}
m3 = {"math" : int(input("Enter the marks of math : "))}

dict.update(m1)
dict.update(m2)
dict.update(m3)

print(dict)