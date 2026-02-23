"""
    Prints an N x N grid with '1' for even (row+col), 
    '0' for odd, and 'X' on the main diagonal.
    Rows and columns are 0-indexed in this example.
"""

# taking user input - in integer format
inp = int(input("Enter a number: "))

# loop for rows
for row in range(inp):
    # loop for columns
    for col in range(inp):
        # when row and columns is same - diagonals (you can analyze it by using any matrix) (because chessboard is like a matrix)
        if row == col:
            print('X', end=' ')
        
        # if it is not diagonal - check the sum of rowValue and columnValue is even (if it is then print '1 ')
        elif (row + col) % 2 == 0:
            print('1', end=' ')
        
        # if it is not diagonal, neither the sum of row and column is even, then just print '0 '
        else:
            print('0', end=' ')

    print() # Move to the next line after each row