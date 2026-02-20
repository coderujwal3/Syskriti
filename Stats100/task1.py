# Task - 1: Find the frequency of the elements in an array
arr = [10,83,18,0,19,69,10,18]
sort_arr = sorted(arr)
freq = {
    sort_arr[0]:1
}
for i in range(1,len(sort_arr)):
    if sort_arr[i] == sort_arr[i-1]:
        freq[sort_arr[i]] += 1
    else:
        freq[sort_arr[i]] = 1
print(f"\n{freq}")


# Task - 2: Find the average of the array
# average refers to mean in statistics

# using the array assigned above (previous task code)
sum = 0
for i in arr:
    sum += i
avg = sum/len(arr)      # mean = sum of all elements / total number of elements
print(f"\nAverage/mean of array: {avg}\n")