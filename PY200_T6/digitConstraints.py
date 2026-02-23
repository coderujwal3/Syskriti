"""
    Finds the smallest number x in 1..N such that:
    - sum of digits of x is divisible by 7
    - x contains exactly two 3s
    - x does not contain digit 0
"""
inp = int(input("Enter a number: "))
flag = 0

for x in range(1, inp + 1):
    s = str(x)
    # Check if x contains digit 0
    if '0' in s:
        continue

    # Check if x contains exactly two 3s
    if s.count('3') != 2:
        continue

    # Check if the sum of digits of x is divisible by 7
    digit_sum = sum(int(digit) for digit in s)
    if digit_sum % 7 == 0:
        flag = 1
        print(x)

if (flag == 0):
    print("-1")