import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    A = int(data[0])
    B = int(data[1])
    d = int(data[2])
    r = int(data[3])
    
    ans = 0
    for x in range(A, B + 1):
        if x % d == r:
            ans += 1
            
    print(ans)

if __name__ == '__main__':
    solve()
