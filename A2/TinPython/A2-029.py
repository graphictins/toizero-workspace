
n = int(input())

for row in range(n):
    line = ""
    for col in range(row + 1):
        # border conditions: left edge, diagonal, bottom row
        if col == 0 or col == row or row == n - 1:
            line += "0"
        else:
            line += "1"
        if col < row:
            line += " "
    print(line)
