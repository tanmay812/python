# leetcode q1
# given an array of integer and an integer target return indices of two number such that they add to the target

n = int(input("Enter the number of element you want :\t"))
arr = []

for i in range(n):
    ele = int(input(f"Enter the {i} element:\t"))
    arr.append(ele)

print(arr)
ind = []


def sum_find(arr, n):
    target = int(input("Enter the target sum:\t"))
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]+arr[j] == target:
                ind.append(i)
                ind.append(j)
        return ind



print(sum_find(arr, n))

