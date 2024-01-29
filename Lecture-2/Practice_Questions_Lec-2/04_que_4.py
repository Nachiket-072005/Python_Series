# WAP to find the gretest of 3 numbers entered by the user

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

if(a > b and a > c):
    print(a, "is greatest")
elif(b > c): 
    print(b, "is greatest")
else: 
    print(c, "is greatest")
    
