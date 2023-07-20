# using the split method

a = "space-space-space"
delimiter = "-"
b = a.split(delimiter)
print(b)
print(delimiter.join(b))

#list comprehnesion
l = [1,2,3]
new = [i*2 for i in l]
print(new)

st = "string"
new = [j for j in st]
print(new)

# list comprehension with if

l = [1,2,3,4,5,6,7,8,9]
new = [i**2 for i in l if i%2==0]
print(new)

a=[1,2,3,4,5]
print(a[3:0])