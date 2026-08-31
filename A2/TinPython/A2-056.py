import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    n = int(data[0])
    arr = [int(x) for x in data[1:n+1]]
    
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
        
    ans = [x for x in counts if counts[x] == 1]
    ans.sort()
    
    if ans:
        print(" ".join(map(str, ans)))
    else:
        print()

if __name__ == '__main__':
    solve()
