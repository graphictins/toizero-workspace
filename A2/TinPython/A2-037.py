
from collections import deque

q = int(input())

emergency = deque()
normal = deque()

for _ in range(q):
    line = input().split()
    cmd = line[0]
    
    if cmd == "ARRIVE":
        name = line[1]
        ptype = line[2]
        if ptype == "emergency":
            emergency.append(name)
        else:
            normal.append(name)
    
    elif cmd == "TREAT":
        if emergency:
            emergency.popleft()
        elif normal:
            normal.popleft()
    
    elif cmd == "SHOW":
        all_patients = list(emergency) + list(normal)
        if all_patients:
            print(' '.join(all_patients))
        else:
            print("EMPTY")
