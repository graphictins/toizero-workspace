

n = int(input().strip())
m = int(input().strip())

a_rows = (n + 1) // 2

for i in range(a_rows):
    print(" ".join(["A"] * m))
for i in range(n - a_rows):
    print(" ".join(["K"] * m))
