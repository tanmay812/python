##
##Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.
# tuple1 = (1, 2, 3)
#tuple2 = (4, 5, 6)
#output_tuple = tuple_elementwise_sum(tuple1, tuple2)
#print(output_tuple)  # Expected output: (5, 7, 9)

n = int(input("Enter the number of elements you want in the tuple:\t"))
n1 = int(input("Enter the number of elements you want in the sec tuple:\t"))
t1 = ()
t2 = ()
for i in range(n):
    ele = int(input("Enter the element:\t"))
    t1 = t1 + (ele,)

print(t1)

for i in range(n1):
    ele = int(input(f"Enter the element {i}:\t"))
    t2 = t2 + (ele,)

print(t2)

def sum_element(t1,t2):
    if len(t1) != len(t2):
        return "can't return is as length of the two tuple not equal"
    result =  tuple(a+b for a,b in zip(t1,t2))
    return result
print("element wise sum :\n",sum_element(t1,t2))
