

x, y = map(int, input().split())
jumps = 0
total = 0
while total < y:
    if x <= 0:
        break
    total += x
    x -= 2
    jumps += 1

if total >= y:
    print(jumps)
else:
    print("-1")
