# implementing selection sort

n = int(input("Enter the number of element you want :\t"))
l = []
for i in range(n):
    ele = int(input("Enter the element you want :\t"))
    l.append(ele)

print(l)

def selection(arr):
    for i in range(len(arr)-1):
        minpos = i #holds the minimum position
        for j in range(i,len(arr)):
            if arr[j] < arr[minpos]:
                minpos = j
        arr[minpos],arr[i] = arr[i],arr[minpos]
    return arr

print("the sorted array:\t",selection(l))
