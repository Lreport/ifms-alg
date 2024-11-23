def isValidSudoku(board):
    # Verifica linhas
    for row in board:
        if not isValidRow(row):
            return False

    # Verifica colunas
    for col in zip(*board):
        if not isValidRow(col):
            return False

    # Verifica subgrades 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not isValidRow(subgrid):
                return False

    return True

def isValidRow(row):
    seen = set()
    for num in row:
        if num != '.' and num in seen:
            return False
        seen.add(num)
    return True

# Exemplo de uso
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print(isValidSudoku(board))  # Saída: True