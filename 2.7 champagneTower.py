def champagneTower(poured, query_row, query_glass):
    tower = [[0] * (i + 1) for i in range(101)] 
    tower[0][0] = poured
    for row in range(100):
        for col in range(row + 1):
            if tower[row][col] > 1:
                overflow = (tower[row][col] - 1) / 2
                tower[row][col] = 1
                tower[row + 1][col] += overflow
                tower[row + 1][col + 1] += overflow
    return min(1, tower[query_row][query_glass])
poured = 1
query_row = 1
query_glass = 1
result = champagneTower(poured, query_row, query_glass)
print(f"Champagne in glass ({query_row}, {query_glass}): {result:.5f}")
