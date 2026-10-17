def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 sub-grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            # Find the first empty cell (represented by 0)
            if board[row][col] == 0:
                # Try numbers from 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        
                        # Recursively continue
                        if solve_sudoku(board):
                            return True
                        
                        # If no solution, backtrack
                        board[row][col] = 0
                        
                return False
    return True

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Sample Sudoku puzzle (0 represents empty cells)
sudoku_board = [
    [0, 0, 9, 5, 8, 6, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 6, 8, 3],
    [9, 0, 0, 6, 5, 0, 0, 3, 2],
    [0, 6, 0, 7, 0, 0, 0, 9, 8],
    [0, 3, 0, 2, 0, 0, 7, 0, 4],
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [6, 2, 0, 0, 1, 5, 0, 4, 0],
    [0, 0, 0, 4, 0, 0, 0, 5, 0]
]

print("Unsolved Sudoku:")
print_board(sudoku_board)
print("\n" + "="*25 + "\n")

if solve_sudoku(sudoku_board):
    print("Solved Sudoku:")
    print_board(sudoku_board)
else:
    print("This Sudoku has no solution.")