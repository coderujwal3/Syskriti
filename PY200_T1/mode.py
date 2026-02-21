"""
    Program to find the mode of the given list of numbers without using any libraries built-in functions
"""


lst = [10,83,18,0,19,69,10,18]
# Dictionary to store the count of each item
counts = {}
for item in lst:
    if item in counts:
        counts[item] += 1  # if the item in list is present in dictionary (counts) then increment the value of that item
    else:
        counts[item] = 1   # if the item is not in list is not present in dictionary (counts) then assign it as a key and its value to 1

# Find the maximum occurrence count
max_count = 0
for item, count in counts.items():      # only iterating on the values of dictionary
    if count > max_count:
        max_count = count

# Extract all items that match that maximum frequency
items_with_max_count = []
for item, freq in counts.items():           # iterating on both keys & values
    if freq == max_count:                   # and add the maximum occurred element in a list
        items_with_max_count.append(item)

# just counting the total number of elements in both list to check that there is any mode or not
count1 = 0
for i in lst:
    count1 += 1

count2 = 0
for i in items_with_max_count:
    count2 += 1

# if the total numbers of elements in given list and items_with_max_count list is same, then there is no mode in the given list
if (count1 == count2):
    print("There is no mode in list")

print(f"Items with maximum occurrence: \n{items_with_max_count}\t:\t{max_count} times")     # output: [10, 18]  :   2 times