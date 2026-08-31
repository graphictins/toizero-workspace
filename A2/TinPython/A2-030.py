
grid = []
for _ in range(5):
    row = list(map(int, input().split()))
    grid.append(row)

bad_row = -1
bad_col = -1

for r in range(5):
    if sum(grid[r]) % 2 != 0:
        bad_row = r

for c in range(5):
    col_sum = sum(grid[r][c] for r in range(5))
    if col_sum % 2 != 0:
        bad_col = c

print(bad_row, bad_col)
