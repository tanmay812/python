# code to find the missing number in the array linear
# find sum of n number of numbers then subtract sum of the array
print("Only for linear arithemetic progression with differnce of one")
n = int(input("Enter the number of element you want in the arrray:\t"))
a = n-1
arr = []

for i in range(a):
    ele = int(input(f"enter the {i} element:\t"))
    arr.append(ele)
print(arr[:])


def missing(arr, n):
    total = (n*(n+1))/2
    sum_arr = sum(arr)
    missing = total - sum_arr
    return missing


print("the missing number in the array is :", missing(arr, n))

