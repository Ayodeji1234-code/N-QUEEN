def print_board(board):
    """Print the chessboard."""
    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col, n):
    """Check if a queen can be placed safely."""

    # Check left side of current row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col, n, solutions):
    """Find all solutions using backtracking."""

    if col == n:
        solution = [row[:] for row in board]
        solutions.append(solution)
        return

    for row in range(n):
        if is_safe(board, row, col, n):

            # Place queen
            board[row][col] = 'Q'

            # Recur for next column
            solve_n_queens(board, col + 1, n, solutions)

            # Backtrack
            board[row][col] = '.'


def main():
    print("=" * 40)
    print("       N-Queens Problem Solver")
    print("=" * 40)

    try:
        n = int(input("Enter the value of N: "))

        if n <= 0:
            print("Please enter a positive integer.")
            return

        # Special case N = 1
        if n == 1:
            print("\nSolution 1:")
            print("Q")
            print("\nTotal Solutions: 1")
            return

        # No solutions for N = 2 or N = 3
        if n in [2, 3]:
            print(f"\nNo solution exists for N = {n}")
            return

        # Create board
        board = [['.' for _ in range(n)] for _ in range(n)]

        # Store all solutions
        solutions = []

        # Solve
        solve_n_queens(board, 0, n, solutions)

        # Display solutions
        print(f"\nFound {len(solutions)} solution(s):\n")

        for index, solution in enumerate(solutions, start=1):
            print(f"Solution {index}:")
            print_board(solution)

        print("=" * 40)
        print(f"Total Solutions: {len(solutions)}")
        print("=" * 40)

    except ValueError:
        print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
    main()