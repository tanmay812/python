# code print dictionary with kays and vlaue interchanged

n = int(input("Enter the number of elements you want in the dictionary:\t"))

dict = {}

for i in range(n):
    key = input("Enter the unique key:")
    value = int(input("Enter the value:\t"))
    dict[key] = value
print(dict)

def reverse_dict(my_dict):
    # TODO
    dict = {}
    for i in my_dict:
        value = i
        key  = my_dict[i]
        dict[key] = value
    return dict

print('The reverse dictionary:\n',reverse_dict(dict))