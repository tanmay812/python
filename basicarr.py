#16 question on 1d array
from array import *

# 1. Create an array and traverse
my_arr = array('i',[ 1,2,3,4,5])
print(my_arr)
for i in range(len(my_arr)):
    print(my_arr[i])
#or
print("\n")
for i in my_arr:
    print(i)

# 2 accessing element through index
a= True

while(a):
    global ind
    ind = int(input("Enter the index of the element :\t"))
    if(ind<0 or ind>=len(my_arr)):
        print("Invalid input try again\n")
    else:
        a=False
print(my_arr[ind],"\n")

#3. appending an element to an array
print("\nStep 3\n")
ele = int(input("Enter the element you want to add:\t"))
my_arr.append(ele) #can only add an element at the end of an array
print(my_arr)

# 4 inserting an element using insert method
print("step 4 : adding element using insert method")
pos = int(input("Enter the postion where you want to add your element :\t"))

my_arr.insert(pos,ele)
print(my_arr)

# using extend method
print("\n5 using extend method")

arr2 = array('i',[10,20,30,40,50])
my_arr.extend(arr2)
print(my_arr)

#adding element using fromlist()
print("\nStep 6")
temp = [31,32,33,34]
my_arr.fromlist(temp)
print(my_arr)

# 7 remove an element from the array
print("\nStep: 7")
rem = int(input("Enter the element to be removed:\t"))
my_arr.remove(rem)
print("\n")
print(my_arr)

#8 removing element using pop method

#pop just removes the last element in an array
my_arr.pop()
print(my_arr)

#index() to find index of an element 

find = int(input("\nEnter the element you want to find:"))
inde = my_arr.index(find)
print("Your element os at index :\t",inde)

#reversing an array using reverse()

my_arr.reverse()
print(my_arr)

#checking number of occurences of an element using count method
cun = int(input("\n Enter the element you want to find the number of occurences of :\t"))
cun1 = my_arr.count(cun)
print(cun1)

#converting an array to list using tolist( ) method
print(my_arr.tolist())
