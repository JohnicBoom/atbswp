# Print this grid with the arrow pointing down.
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
# Nested loop
#	Outside loop starts at the 1st column (0) and counts up
for column in range(len(grid[0])):
#	Inside loop starts at the 9th row (8) and counts down
    for row in range(len(grid) - 1, -1, -1):
#	Use print with "end=''" to prevent new lines when printing rows
#	Print column 0, row 8 - then column 0, row 7 - etc.
        print(grid[row][column], end='')
#	Print '' at the end of the inside loop
    print('')