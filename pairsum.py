#code to print array of pairs of number which is equal to given sum
n = int(input("Enter the number of element you want in the array:\t"))
arr = []
for i in range(n):
    ele = int(input("Enter the element you want:\t"))
    arr.append(ele)
print(arr)
sum  = int(input("Enter the sum:\t"))
def pair_sum(myList, sum):
    # TODO
    ext = []
    for i in range(len(myList)):
        for j in range(i,len(myList)):
            if myList[i] + myList[j] == sum:
                st = str(f"{myList[i]}+{myList[j]}")
                ext.append(st)
    return ext

print(pair_sum(arr,sum))