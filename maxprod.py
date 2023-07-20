#code to get the max product of two numbers in an array of positive numbers

n = int(input("Enter the number of element you want in the array:\t"))
arr = []
for i in range(n):
    ele = int(input("Enter the element you want:\t"))
    arr.append(ele)

print(arr)

def great(arr,n):
    max1 = 0
    max2 = 0

    for i in arr:
        if i>max1:
            max2 = max1
            max1 = i
        elif i>max2 :
            max2= i
    return max1*max2

print("The max product of two number in an array :\t",great(arr,n))

