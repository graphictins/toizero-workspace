
n, m = map(int, input().split())
k = int(input())

# count pokemon per cell
poke_count = {}
for _ in range(k):
    r, c = map(int, input().split())
    poke_count[(r, c)] = poke_count.get((r, c), 0) + 1

# try every empty cell as standing position
best = 0
for sr in range(n):
    for sc in range(m):
        if (sr, sc) in poke_count:
            continue  # can't stand on pokemon cell
        total = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                neighbor = (sr + dr, sc + dc)
                total += poke_count.get(neighbor, 0)
        best = max(best, total)

print(best)
