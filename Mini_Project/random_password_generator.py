import random
import string

pass_len = 8
charValues = string.ascii_letters + string.digits + string.punctuation

#list comprehension [function for i in range(n)] -> another method to solve this.

password = "".join([random.choice(charValues) for i in range(pass_len)])

# first method

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)

print("Your password is : ", password)