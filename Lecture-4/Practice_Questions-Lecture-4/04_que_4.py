# Figure out a way to store 9 & 9.0 as separate value in the set.(You can help of built-in data types)

# First methods
values = {
    ("int", 9),
    ("float", 9.0)
}
print(values)

# Second methods
set = {'9.0', 9}
print(set)