# finding a number in an array

import numpy as np
n = int(input("Enter the number of element you want in the array:\t"))
arr = []
for i in range(n):
    ele = int(input("Enter the element you want:\t"))
    arr.append(ele)
np_arr = np.array(arr)

print(np_arr)

def find(np_arr,n):
    target = int(input("Enter the target element:\t"))
    for j in range(n):
        if np_arr[j] == target:
            return j
    return -1

print("The element is at the index ", find(np_arr,n))


