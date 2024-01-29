a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))
d = int(input("Enter the value of d : "))

if(a > b and a > c and a > d): 
    print(a, "is max")
elif(b > c and b > d): 
    print(b, "is max")
elif(c > d):
    print(c, "is max")
else: 
    print(d, "is max")