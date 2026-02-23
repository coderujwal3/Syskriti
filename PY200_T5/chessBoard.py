"""
    Prints an N x N grid with '1' for even (row+col), 
    '0' for odd, and 'X' on the main diagonal.
    Rows and columns are 0-indexed in this example.
"""
inp = int(input("Enter a number: "))
for row in range(inp):
    for col in range(inp):
        if row == col:
            print('X', end=' ')
        elif (row + col) % 2 == 0:
            print('1', end=' ')
        else:
            print('0', end=' ')
    print() # Move to the next line after each row