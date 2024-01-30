# WAP to check if a list contains palindrome of elements.(Hint : use copy() method)

list1 = [1, 2, 3, 2, 1]
list2 = [1, "abc", "abc", 1]

copyList1 = list1.copy()
copyList2 = list2.copy()

copyList1.reverse()
if(list1 == copyList1):
    print("Yes, Lists are contains palindrome elements")
else:
    print("No, Lists are not contain palindrome elements")

copyList2.reverse()
if(list2 == copyList2):
    print("Yes, Lists are contains palindrome elements")
else:
    print("No, Lists are not contain palindrome elements")
