def matrix_chain_order(dimensions):
    n = len(dimensions) - 1  # Number of matrices
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for chain_length in range(2, n + 1):
        for i in range(1, n - chain_length + 2):
            j = i + chain_length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dimensions[i - 1][0] * dimensions[k][1] * dimensions[j][1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s

def print_optimal_parenthesization(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parenthesization(s, i, s[i][j])
        print_optimal_parenthesization(s, s[i][j] + 1, j)
        print(")", end="")

# Example usage:
matrix_dimensions = [(2, 3), (3, 4), (4, 2)]
m, s = matrix_chain_order(matrix_dimensions)

print("Optimal Parenthesization:")
print_optimal_parenthesization(s, 1, len(matrix_dimensions) - 1)
print("\nMinimum number of scalar multiplications:", m[1][len(matrix_dimensions) - 1])
