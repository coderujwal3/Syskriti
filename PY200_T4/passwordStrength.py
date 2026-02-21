"""
    Program to check the password is STRONG or WEAK, by using conditional statements. For a valid password the criteria's are:
    - Length of password should be 8 characters long
    - Must have at least 1 uppercase character
    - Must have at least 1 lowercase character
    - Must have at least 1 digit
"""



print(f"{"-"*30}\nFor Valid password your password should be -\n\t- at least 8 characters long\n\t- 1 uppercase character\n\t- 1 lowercase character\n\t- and 1 digit character\n{"-"*30}\n")
inp = input("Enter the password: ")

if len(inp) >= 8:
    if(any(i.isdigit() for i in inp)):
        if(any(i.isupper() for i in inp)):
            if(any(i.islower() for i in inp)):
               print("Password is valid (STRONG)")
            else:
                print("Password is not valid (WEAK)")
                print("Password must have 1 lowercase character")
        else:
            print("Password is not valid (WEAK)")
            print("Password must have 1 uppercase character")
    else:
        print("Password is not valid (WEAK)")
        print("Password must have 1 digit")
else:
    print("\nPassword is WEAK")
    print("Password must be 8 characters long")