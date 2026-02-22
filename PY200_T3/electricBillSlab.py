"""
    Program to find the cost of the Electricity Bill slab:
    - TaskPY200_T3: Write program to calcite Electricity Bill Slabs. User enters a bill unit and gets the total bill according to following logic. Input: units Rates: • First 100 @ 2/unit • Next 100 (101 – 200) @ 3/unit • Next 300 (20 – 500) @ 5/unit • Above 500 @ 8/unit Add fixed charge 50 if units > 0 Print total bill
"""

# taking the user input, how many units
inp = int(input("Enter the Units: "))

bal = inp       # to calculate the balance in each condition
bill = 0        # to calculate the total bill


if (inp > 0):       # initial check - the number units can not be negative
    bill += 50      # fixed charge - as mentioned in task description (if units > 0)

    if(inp > 100):              # for first 100 in whole number of units
        bal = inp - 100         # deducting the first 100 from balance
        bill += 100 * 2         # incremented the bill according to the condition (@ 2/unit)

        if (bal > 100):         # for next 100 in whole number of units (101 to 200)
            bal = bal - 100     # deducting 100 units again from balance
            bill += (100 * 3)   # incremented the bill according to the condition (@ 3/unit)

            if(bal > 300):              # for next 300 in whole number of units (201 to 500)
                bal = bal - 300         # deducting 300 units again from balance
                bill += (300 * 5)       # incremented the bill according to the condition (@ 5/unit)

                bill += (bal * 8)       # Here we find out the units are greater than 500 so, the bill will be incremented according to the condition (above 500 @ 8/unit)  
            else:
                bill += (bal * 5)       # the balance is not greater than 300, then just calculate the balance amount with the condition (its between 201 to 500 - @ 5/unit)
        else:
            bill += (bal * 3)           # the balance is not greater than 200, then just calculate the balance amount with the condition (its between 101 to 200 - @ 3/unit)
    else:
        bill += inp * 2          # the balance is not greater than 100, then just calculate the balance amount with the condition (first 100 - @ 2/unit)
else:
    print("Units can not be negative")


# print the total cost of the bill
print(f"Electric slab bill: {bill}")