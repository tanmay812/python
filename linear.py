#linear search in python

n = int(input("enter the numberof element you want:\t"))
arr = []
for i in range(n):
    ele = int(input("Enter the element you want:\t"))
    arr.append(ele)

print(arr)
target = int(input("Enter the element you want to search:\t"))

def linear(arr,target):
    for i,val in enumerate(arr):
        if val == target:
            return i
    return -1

print("The index of the element is :\t",linear(arr,target))