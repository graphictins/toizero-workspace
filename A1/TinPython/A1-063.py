

import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

T = int(input_data[0])
idx = 1
while idx < len(input_data):
    age = int(input_data[idx])
    tickets = int(input_data[idx+1])
    idx += 2
    
    if age < 15:
        print("-1")
        continue
    
    if T < tickets:
        print("-2")
        continue
    
    total = tickets * 150
    if 15 <= age <= 22:
        total = int(total * 0.8)
    elif age >= 60:
        total = int(total * 0.5)
        
    T -= tickets
    print(f"{total} {T}")
