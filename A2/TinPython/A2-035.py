
n = int(input())
items = []
for _ in range(n):
    items.append(input().strip())

result = []

def permute(current, remaining):
    if not remaining:
        result.append(' '.join(current))
        return
    for i in range(len(remaining)):
        permute(current + [remaining[i]], remaining[:i] + remaining[i+1:])

permute([], items)

for perm in result:
    print(perm)
print(len(result))
