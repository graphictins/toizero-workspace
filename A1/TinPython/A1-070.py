

import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

n = int(input_data[0])
idx = 1
for _ in range(n):
    if idx + 2 >= len(input_data):
        break
    p = float(input_data[idx])
    c = float(input_data[idx+1])
    g = float(input_data[idx+2])
    idx += 3
    
    total = p + c + g
    ans = [f"{total:.1f}"]
    
    if total > 50.0:
        ans.append("Overloaded")
        
    if p > 20.0:
        ans.append("Check Type Plastic")
    if c > 20.0:
        ans.append("Check Type Can")
    if g > 20.0:
        ans.append("Check Type Glass")
        
    print(",".join(ans))
