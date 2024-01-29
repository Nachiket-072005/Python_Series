str = "i am a coder"

# endswith() -> It will return true if string ends with sub string
print(str.endswith("er")) #True
print(str.endswith("ar")) #False

# capitalize() -> It will capitalize 1st characater of string. This function will make copy of string. It will not affect the our original string.
print(str.capitalize())

# replace() -> It will replace old sub string to New sub string
print(str.replace("a", "o"))
print(str.replace("coder", "programmer"))

# find() -> It will return 1st index of 1st occurance. If It dosn't find then return -1 index.
print(str.find("o"))
print(str.find("coder"))
print(str.find("q"))

# count() -> It will count the occurance of sub string in string.
print(str.count("a"))
print(str.count("coder"))