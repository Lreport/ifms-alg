def sum_diagonals_matriz_quadratic(matriz):
    sum = 0
    for i in range(len(matriz)):
        sum += matriz[i][i] + matriz[i][len(matriz) - i - 1]
    return sum

def main():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sum_diagonals_matriz_quadratic(matriz))

#input num matriz

main()