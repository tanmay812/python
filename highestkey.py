# Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

# Example:

#dict1 = {'a': 1, 'b': 2, 'c': 3}
#dict2 = {'b': 3, 'c': 4, 'd': 5}
#merge_dicts(dict1, dict2)
# Output:

n = int(input("Enter the number of elements you want in the dictionary:\t"))

dict = {}

for i in range (n):
    key = input("Enter the unique key:")
    value  = int(input("Enter the value:\t"))
    dict[key] = value
print(dict)

def max_key(dict):
    return max(dict,key=dict.get)

print("The maximum value is with the key:\t",max_key(dict))
