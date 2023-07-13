# creation of a two d array

import numpy as nu
arr1 = nu.array([[11, 15, 10, 6], [10, 14, 11, 5],
                [12, 17, 12, 8], [15, 18, 14, 9]])
print(arr1)

# inserting element into 2d array
newarr = nu.insert(arr1, 0, [1, 2, 3, 4], axis=0)
print(newarr)

# accessing element from 2d array


def access(array, rowind, colind):
    if rowind >= len(array) or colind >= len(array[0]):
        return 0
    else:
        return(array[rowind][colind])


rowind = int(input("Enter the index of the row you want:\t"))
colind = int(input("Enter the index of the column you want:\t"))
print(access(newarr, rowind, colind))

# traversing through the 2d array

for i in range(len(newarr)):
    for j in range(len(newarr[0])):
        print(newarr[i][j])

# searching through the array

ele = int(input("Enter the element you want to search:\t"))


def search(array, ele):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if(array[i][j] == ele):
                print(i,j)
    
search(newarr,ele)

#deletion in two d array
print(newarr)
print("\n")
newarr1 = nu.delete(newarr,0,axis=0)
print(newarr1)