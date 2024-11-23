str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
index = int(input("Enter the index at which you want to concatenate the string2: "))
finalStr = str1[0:index] + str2 + " " + str1[index:len(str1)]
print(finalStr)