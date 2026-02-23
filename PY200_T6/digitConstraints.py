"""
    Finds the smallest number x in 1..N such that:
    - sum of digits of x is divisible by 7
    - x contains exactly two 3s
    - x does not contain digit 0
"""

# taking the user input
inp = int(input("Enter a number: "))
# using this flag later on for checking that there is any element or not which satisfies the condition
flag = 0

# iterating from 1 to input's number +1 (input number of times) (if inp = 5 then 5 times)
for x in range(1, inp + 1):
    
    # Convert x to a string
    s = str(x)

    # Check if x contains digit 0
    if '0' in s:
        continue    # jump the iteration, when hitting this condition

    # Check if x contains exactly two 3s
    if s.count('3') != 2:
        continue    # jump the iteration, when hitting this condition

    # Initialize the total sum to zero
    digit_sum = 0
    # iterating through string 's' and add the all integers in that string one-by-one
    for digit in s:
        digit_sum += int(digit)
    
    # Check if the sum of digits of x is divisible by 7
    if digit_sum % 7 == 0:
        flag = 1        # if any 1 answer is also found, then make the flag 1 (true) - which means that there is any final answer exist, we don't have to print -1
        print(x)

# when there is no value existing in the range, then print '-1'
if (flag == 0):
    print(-1)