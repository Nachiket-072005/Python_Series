fullName=input("Enter your full name with space separated: ")
indexOfSpace = fullName.index(" ")
firstName = fullName[0:indexOfSpace]
lastName = fullName[indexOfSpace + 1: len(fullName)]

print(f"First Name: {firstName}")
print(f"Last Name: {lastName}")
print(f"Full Name: {fullName}")