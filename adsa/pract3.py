def is_safe(board, row, col, n):
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower left diagonal
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(n):
    def solve(board, col):
        if col >= n:
            solutions.append([row[:] for row in board])
            return

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve(board, col + 1)
                board[i][col] = 0

    board = [[0] * n for _ in range(n)]
    solutions = []
    solve(board, 0)
    return solutions

def print_chessboard(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))

# Input: N (size of the chessboard and number of queens)
N = int(input("Enter the size of the chessboard (N): "))
if N < 4:
    print("N should be greater than or equal to 4.")
else:
    solutions = solve_n_queens(N)
    print(f"All solutions for {N}-Queens problem:")
    for idx, solution in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        print_chessboard(solution)
        print()
