

import sys

def solve():
    # Read N and K
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    # Read S_i values
    s = [int(x) for x in input_data[2:]]
    
    # Identify the fastest runner (S_min)
    s_min = min(s)
    
    # K = 1 means no one can be lapped
    if k == 1:
        print(n)
        return

    # Total time for the winner to finish K laps
    # T_win = s_min * k
    winner_total_time = s_min * k
    
    count = 0
    # A runner stays in if they finish lap (K-1) 
    # strictly before the winner finishes lap K.
    # Logic: s[i] * (k - 1) < s_min * k
    for si in s:
        if si * (k - 1) < winner_total_time:
            count += 1
            
    print(count)

if __name__ == "__main__":
    solve()