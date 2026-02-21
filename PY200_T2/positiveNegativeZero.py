"""
    Program to check the given input is positive, negative or zero integer value
"""

inp = int(input("Enter the number: "))

if inp > 0:
    print(f"{inp} is Positive Integer, however its Negative value is {inp*-1}")
elif inp < 0:
    print(f"{inp} is Negative Integer, however its Positive value is {inp*-1}")
else:
    print(f"{inp} is 0 (zero)")