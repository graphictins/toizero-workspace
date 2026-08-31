

Str = input().strip()
x, y = 0, 0


# loop through each character in the string
for character in Str:
    if character == 'N':
        y += 1
    elif character == 'S':
        y -= 1
    elif character == 'E':
        x += 1
    elif character == 'W':
        x -= 1

print(f"{x} {y} {abs(x) + abs(y)}")
