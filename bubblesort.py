# implementing bubble sort

n = int(input("Enter the number of element you want :\t"))
l = []
for i in range(n):
    ele = int(input("Enter the element you want :\t"))
    l.append(ele)

print(l)


def bubble(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print("The sorted array is :\t", bubble(l))
