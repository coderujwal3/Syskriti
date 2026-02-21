# median of statistics Program
lst = [10,83,18,0,19,69,10,18]
count = 0           # to count the number of elements in it
for i in lst:
    count += 1      # counting the number of elements in list

if count%2 == 0:    # if the length of list (or the number of elements is even)
    med_idx = count//2                              # then find the middle index (the size is even so you will get the middle index + 1)
    median = (lst[med_idx-1] + lst[med_idx])/2      # the formula to find the median (sum of both indices and divide it by 2)
else:
    med_idx = count//2              # if the total number of elements is odd
    median = lst[med_idx]           # then the median value is the middle of the index

print(f"\nMedian of list: {median}\n")      # output - 9.5