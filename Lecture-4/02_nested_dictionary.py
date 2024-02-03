student = {
    "name" : "Nachiket",
    "sub_score" : {
        "phy" : 85,
        "chem" : 81,
        "math" : 90
    } 
}

# print(student["sub_score"]["math"])
# return all keys in the form of Lists
print(len(list(student.keys())))
# return all the values in the form of Lists
print(list(student.values()))
# return all the key, value pairs in the form of tuples
pairs = list(student.items())
print(pairs[0], pairs[1])
# return the value according to key 

"""
Difference between Normal method to fetch the value & Using method to get the value
"""
print(student["name"]) # If we have written key is wrong then, It will return error
print(student.get("name")) # This will not give error -> This will give none value

# insert the specified items to the dictionary 
new_dict = {"name" : "Nachiket Prajapati", "age" : 19}
student.update(new_dict)
print(student)