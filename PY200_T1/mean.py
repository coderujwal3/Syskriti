"""
    Program to find the mean of the given list of numbers without using any libraries built-in functions
"""

# average refers to mean in statistics
lst = [10,83,18,0,19,69,10,18]
count = 1           # to count the number of elements in it
sum = 0             # to add all the elements
for i in lst:
    sum += i
    count += 1
mean = sum/count      # mean = sum of all elements / total number of elements
print(f"\nAverage/mean of array: {mean}\n")         # the output - 25.22222222222222
print(f"\nAverage/mean of array with 2 decimal values: {mean:.2f}\n")     # the output which will contain only 2 decimal places - 25.22