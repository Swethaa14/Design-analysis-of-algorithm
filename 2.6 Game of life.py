def gameOfLife(board):
    m, n = len(board), len(board[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    original = [[board[i][j] for j in range(n)] for i in range(m)]
    def countLiveNeighbors(i, j):
        live_neighbors = 0
        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n and original[ni][nj] == 1:
                live_neighbors += 1
        return live_neighbors
    for i in range(m):
        for j in range(n):
            live_neighbors = countLiveNeighbors(i, j)
            if original[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[i][j] = 0
            elif original[i][j] == 0 and live_neighbors == 3:
                board[i][j] = 1
board1 = [[0, 1, 0],
          [0, 0, 1],
          [1, 1, 1],
          [0, 0, 0]]
gameOfLife(board1)
print("Next state of the board:")
for row in board1:
    print(row)
