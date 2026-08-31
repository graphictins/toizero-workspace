

import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    
    n = int(data[0])
    # Sort descending to pick the furthest for the "one-way" trip in each group
    x = sorted([int(v) for v in data[1:]], reverse=True)
    
    # dp[i] = minimum energy to deliver the first i items
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    # Iterate through each available drone (1 to 200)
    for d in range(1, 201):
        prev_dp = list(dp)
        for i in range(n):
            if prev_dp[i] == float('inf'): continue
            
            # Drone d takes k items (1 to 10)
            for k in range(1, 11):
                if i + k > n: break
                
                # The furthest in this group is x[i] (due to reverse sort)
                # This item is the "one-way" trip. Others are "round trips".
                sub_group = x[i:i+k]
                energy = d * (sub_group[0] + 2 * sum(sub_group[1:]))
                
                if prev_dp[i] + energy < dp[i+k]:
                    dp[i+k] = prev_dp[i] + energy
                    
    print(int(dp[n]))

if __name__ == "__main__":
    solve()