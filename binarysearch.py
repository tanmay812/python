# binery search
# dividing the array in half

n = int(input("Enter the number of element you want in the list:\t"))
l = []
for i in range(n):
    enter = int(input("Enter the element:\t"))
    l.append(enter)
l.sort()
print(l)
def search(arr1, ele):
    low = 0
    u = len(arr1)-1
    while low <= u:
        mid = (low+u)//2
        if arr1[mid] == ele:

            return mid
        else:
            if arr1[mid] < ele:
                low = mid
            elif arr1[mid] > ele:
                u = mid

ele = int(input("Enter the element you want to find in the list:\t"))
print("element is at the index:\t",search(l,ele))