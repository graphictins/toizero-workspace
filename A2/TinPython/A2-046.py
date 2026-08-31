import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines: return
    t = int(lines[0].strip())
    
    vowels = set("aeiouAEIOU")
    
    for i in range(1, t + 1):
        if i < len(lines):
            line = lines[i]
            v_count = 0
            max_conseq = 0
            cur_conseq = 0
            for char in line:
                if char in vowels:
                    v_count += 1
                    cur_conseq += 1
                    if cur_conseq > max_conseq:
                        max_conseq = cur_conseq
                else:
                    cur_conseq = 0
            
            print(f"Line {i}: vowels = {v_count}, max_consecutive = {max_conseq}")

if __name__ == '__main__':
    solve()
