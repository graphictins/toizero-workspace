import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    A = []
    B = []
    for i in range(3):
        A.append([int(data[i*3]), int(data[i*3+1]), int(data[i*3+2])])
    for i in range(3):
        B.append([int(data[9+i*3]), int(data[9+i*3+1]), int(data[9+i*3+2])])
        
    m = (1 << 15) + 9
    C = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            val = 0
            for k in range(3):
                val += A[i][k] * B[k][j]
            C[i][j] = val % m
            
    for i in range(3):
        print(" ".join(map(str, C[i])))

if __name__ == '__main__':
    solve()
