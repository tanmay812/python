# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

# DO NOT allocate another 2D matrix and do the rotation.

n = int(input("Enter the number of element you want in the array:\t"))
arr = []
for i in range(n):
    col = []
    for j in range(n):
        ele = int(input(f"Enter the element {i} {j}:\t"))
        col.append(ele)
    arr.append(col)
print(arr)
for i in range(n):
    print(arr[i])


def rotate(matrix):
    # TODO
    n = len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix

for i in range(n):
    print(rotate(arr)[i])

