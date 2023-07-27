# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

n = int(input("Enter the number of element you want in a list:\t"))

list1 = []
list2 = []

for i in range(n):
    ele = int(input("Enter the elements for list1:\t"))
    list1.append(ele)
print(list1)

for j in range(n):
    elem = int(input("Enter the elements for list1:\t"))
    list1.append(elem)
print(list2)


def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter

    return count_elements(list1) == count_elements(list2)


print("Checking:\t", check_same_frequency(list1, list2))
