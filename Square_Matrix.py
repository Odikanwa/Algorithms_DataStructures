"""Given a square matrix, calculate the absolute difference between the sums of its diagonals. 
For example, the square matrix ar = [1, 2, 3, 4, 5, 6 , 7, 8, 9], arranged in a 3×3 grid resembling a phone keypad."""
def diagonal_difference(matrix):
    n = len(matrix)  # Assuming it's a square matrix
    primaryDiagonalSum = 0
    secondaryDiagonalSum = 0

    for i in range(n):
        primaryDiagonalSum += matrix[i][i]
        secondaryDiagonalSum += matrix[i][n - i - 1]

    absoluteDifference = abs(primaryDiagonalSum - secondaryDiagonalSum)
    return absoluteDifference

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = diagonal_difference(matrix)
print("Absolute difference between diagonals:", result, len(matrix))

"""Given a square matrix, calculate the sum of its diagonals. 
Only include the sum of the elements in the primary diagonal and all the elements in the secondary diagonal that
are not part of the primary diagonal.

For example, the square matrix ar = [1, 2, 3, 4, 5, 6 , 7, 8, 9], arranged in a 3×3 grid resembling a phone keypad."""

def diagonal_sum(matrix):
    n = len(matrix)
    primaryDiagonalSum = 0
    secondaryDiagonalSum = 0
    
    for i in range(n):
        primaryDiagonalSum += matrix[i][i]
        secondaryDiagonalSum += matrix[i][n-i-1]
    
    sum_of_diagonals = (primaryDiagonalSum + secondaryDiagonalSum) - (matrix[n//2][n//2] if n % 2 else 0)
    return sum_of_diagonals

example2 = diagonal_sum(matrix)
print(example2)