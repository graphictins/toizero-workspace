
n = int(input())
max_weight = -1
max_name = ""
over_count = 0

for _ in range(n):
    parts = input().split()
    name = parts[0]
    weight = int(parts[1])
    if weight > 15:
        over_count += 1
    if weight > max_weight:
        max_weight = weight
        max_name = name

print(over_count)
print(max_name, max_weight)
