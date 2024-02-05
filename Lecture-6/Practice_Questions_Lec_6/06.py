# WA recursive function to calculate the sum of the first n natural numbers.

def cal_Sum(n):
    if(n == 0):
        return 0
    return cal_Sum(n - 1) + n

print(cal_Sum(10))

