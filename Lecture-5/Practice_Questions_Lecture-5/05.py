# Search for a number x in this tuples using loop : 

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49

i = 0
while i < len(nums) : 
    if(nums[i] == x) :
        print("Found at idx ", i)
        break
    else :
        print("Finding....")
    i += 1 
