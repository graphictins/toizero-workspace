import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    s = data[0]
    x_str = ""
    for c in s:
        if c.isdigit():
            x_str += c
        else:
            break
    x = int(x_str)
    k = s[len(x_str):].upper()
    
    mid1 = (x - 1) // 2
    mid2 = x // 2
    
    for r in range(x):
        d = min(abs(r - mid1), abs(r - mid2))
        if k == '#':
            char = '#'
        else:
            pos = (ord(k) - ord('A')) + d
            cycle_pos = pos % 50
            if cycle_pos <= 25:
                val = cycle_pos
            else:
                val = 50 - cycle_pos
            char = chr(ord('A') + val)
            
        row = ['-'] * x
        row[d] = char
        row[x - 1 - d] = char
        print("".join(row))

if __name__ == '__main__':
    solve()
