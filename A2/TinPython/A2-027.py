
n = int(input())
scores = []
for _ in range(n):
    scores.append(int(input()))

top = max(scores)
count = scores.count(top)
print(top)
print(count)
