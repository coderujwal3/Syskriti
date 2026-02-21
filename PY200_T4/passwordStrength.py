"""
    Program to check the password is STRONG or WEAK, by using conditional statements. For a valid password the criteria's are:
    - Length of password should be 8 characters long
    - Must have at least 1 uppercase character
    - Must have at least 1 lowercase character
    - Must have at least 1 digit
"""


inp = input("Enter the password: ")

if len(inp) >= 8:
    if(any(i.isdigit() for i in inp) and any(i.isupper() for i in inp) and any(i.islower() for i in inp)):
        print("Password is valid (STRONG)")
    else:
        print("Password is not valid (WEAK)")
        print("For Valid password your password should be -\n\tat least 8 characters long\n\t1 uppercase character\n\t1 lowercase character\n\tand 1 digit\n")
else:
    print("\nPassword is WEAK")
    print("For Valid password your password should be -\n\tat least 8 characters long\n\t1 uppercase character\n\t1 lowercase character\n\tand 1 digit\n")