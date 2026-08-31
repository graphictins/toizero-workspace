import sys

def solve():
    import sys
    lines = sys.stdin.read().split('\n')
    if not lines: return
    s = lines[0].rstrip('\r')
    if not s: return
    
    first = ord(s[0].upper())
    last = ord(s[-1].upper())
    l = len(s)
    
    res = []
    for i in range(1, 11):
        v = i - 1
        if i % 2 != 0:
            val = first + v
        else:
            val = last - v
            
        val = val % l
        if val > 9:
            val = val % 10
        res.append(val)
        
    ans = res[2:8]
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    solve()
