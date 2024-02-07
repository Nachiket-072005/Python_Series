count = 0
with open("sample.txt", "r") as f:
    data = f.read()
    # print(data)
    # print(type(data))

    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
        
print(count)