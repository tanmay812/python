#code to remove the duplicate element in the array


n = int(input("Enter the number of element you want in the array:\t"))
arr = []
for i in range(n):
    ele = int(input("Enter the element you want:\t"))
    arr.append(ele)
print(arr)
def rem_duplicate(arr):
    rem = []
    for i in arr:
        if i not in rem:
            rem.append(i)
    return rem

print("array after removing the duplicate items:\t",rem_duplicate(arr))

