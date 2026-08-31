import sys

def solve():
    # Read all input data
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    L = int(input_data[1])
    
    intervals = []
    idx = 2
    for _ in range(N):
        s = int(input_data[idx])
        t = int(input_data[idx + 1])
        intervals.append((s, t))
        idx += 2
        
    # Step 1: Sort by ending point (T_i)
    intervals.sort(key=lambda x: x[1])
    
    point_count = 0
    last_point = -1 # Position of the last placed toll point
    
    for s, t in intervals:
        # Step 2: Check if current interval is already covered
        # It is covered if the last_point is between s and t
        if last_point < s:
            # Step 3: Place a new point at the end of the current interval
            point_count += 1
            last_point = t
            
    print(point_count)

if __name__ == "__main__":
    solve()