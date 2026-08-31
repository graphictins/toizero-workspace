
n = int(input())

A = []
for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

B = []
for _ in range(n):
    row = list(map(int, input().split()))
    B.append(row)

for i in range(n):
    print(' '.join(str(A[i][j] + B[i][j]) for j in range(n)))
