# N-Queens Problem Solver

## Description

The N-Queens Problem Solver is a Python application that uses a backtracking algorithm to place N queens on an N × N chessboard such that no two queens can attack each other. The program represents the chessboard as a 2D array and systematically explores valid positions to find all possible solutions.

This project demonstrates the use of recursion, backtracking, and constraint satisfaction techniques in solving a classic computer science problem.

## Features

* Accepts any positive integer value for N
* Represents the chessboard using a 2D array
* Uses backtracking to find valid queen placements
* Ensures no two queens share the same row, column, or diagonal
* Displays all possible solutions
* Counts and displays the total number of solutions
* Handles special cases for N = 1, N = 2, and N = 3
* User-friendly console interface

## Technologies Used

* Python 3

## How It Works

The program places queens one column at a time. Before placing a queen, it checks whether the position is safe by verifying:

* No queen exists in the same row
* No queen exists on the upper-left diagonal
* No queen exists on the lower-left diagonal

If a safe position is found, the queen is placed and the algorithm moves to the next column. If no safe position exists, the algorithm backtracks and tries a different arrangement.

## Installation

1. Ensure Python 3 is installed on your computer.
2. Download or clone the project files.
3. Open a terminal or command prompt in the project directory.

## Usage

Run the program using:

```bash
python n_queen.py
```

Enter the value of N when prompted.

Example:

```text
Enter the value of N: 4
```

## Sample Output

```text
========================================
       N-Queens Problem Solver
========================================
Enter the value of N: 4

Found 2 solution(s):

Solution 1:
. . Q .
Q . . .
. . . Q
. Q . .

Solution 2:
. Q . .
. . . Q
Q . . .
. . Q .

========================================
Total Solutions: 2
========================================
```

## Algorithm

The solution is based on the Backtracking Algorithm:

1. Start from the first column.
2. Place a queen in a safe row.
3. Move to the next column.
4. If no safe position exists, backtrack to the previous column.
5. Continue until all queens are placed successfully.
6. Store and display each valid solution found.

## Time Complexity

The worst-case time complexity is approximately:

```text
O(N!)
```

This is because the algorithm explores different arrangements of queens while pruning invalid positions through backtracking.

## Learning Outcomes

This project helped strengthen my understanding of:

* Recursion
* Backtracking algorithms
* Constraint satisfaction problems
* 2D arrays and matrix representation
* Algorithm design and optimization
* Problem-solving techniques in Python

## Future Improvements

* Graphical visualization of the chessboard
* Display queens using Unicode symbols (♕)
* Save solutions to a file
* Compare performance for different board sizes
* Interactive GUI version using Tkinter or PyQt

## Author

Developed as part of my Python Development Internship project.
