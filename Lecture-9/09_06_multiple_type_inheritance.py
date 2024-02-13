class A:
    var1 = "Welcome to the class A"

class B:
    var2 = "Welcome to the class B"

class C(A, B):
    var3 = "Welcome to the class C"

c = C()

print(c.var1)
print(c.var2)
print(c.var3)