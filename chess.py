"""
Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for
the first cell, and then the last two - for the second cell.
"""

col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

if (col1 + row1) % 2 == 0 and (col2 + row2) % 2 == 0:
    print("YES")
elif (col1 + row1) % 2 != 0 and (col2 + row2) % 2 != 0:
    print("YES")
else:
    print("NO")

"""
In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard, determine 
whether a bishop can go from the first to the second in one move.
The program receives as input four numbers from 1 to 8, specifying the column and row numbers of the starting square and 
the column and row numbers of the ending square. The program should output YES if a Bishop can go from the first square 
to the second in one move, or NO otherwise.
"""

col_from = int(input())
row_from = int(input())
col_to = int(input())
row_to = int(input())

if abs(col_from - col_to) == abs(row_from - row_to):
    print("YES")
else:
    print("NO")

"""
Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the 
chessboard, determine whether a queen can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for 
the first cell, and then the last two - for the second cell. The program should output YES if a queen can go from the 
first cell to the second in one move, or NO otherwise.
"""

col_from = int(input())
row_from = int(input())
col_to = int(input())
row_to = int(input())

if abs(col_from - col_to) == abs(row_from - row_to):
    print("YES")
elif col_from == col_to or row_from == row_to:
    print("YES")
else:
    print("NO")