class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        # Check if there's a queen in the same column
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve_n_queens(self, row):
        if row == self.n:
            # Convert board to a printable solution
            solution = [''.join('Q' if cell == 1 else '.' for cell in row) for row in self.board]
            self.solutions.append(solution)
            return True

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                if self.solve_n_queens(row + 1):
                    self.board[row][col] = 0  # backtrack
                else:
                    self.board[row][col] = 0

        return False

    def find_solutions(self):
        self.solve_n_queens(0)
        return self.solutions

def main():
    n = int(input("Enter the size of the chessboard (n x n): "))
    n_queens = NQueens(n)
    solutions = n_queens.find_solutions()

    if solutions:
        print(f"Found {len(solutions)} solutions for {n}-queens problem:")
        for idx, solution in enumerate(solutions, start=1):
            print(f"Solution {idx}:")
            for row in solution:
                print(row)
            print()
    else:
        print("No solutions found for the n-queens problem.")

if __name__ == "__main__":
    main()
