import sys
from collections import deque

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    n = int(input_data[ptr]); ptr += 1
    m = int(input_data[ptr]); ptr += 1
    
    # rule_counts[i] = number of bulbs still needed for rule i to trigger
    rule_counts = []
    # rule_target[i] = the bulb that turns on if rule i triggers
    rule_target = []
    # adj[bulb] = list of rule indices that depend on this bulb
    adj = [[] for _ in range(n + 1)]
    
    for i in range(m):
        k = int(input_data[ptr]); ptr += 1
        needed = []
        for _ in range(k):
            bulb = int(input_data[ptr]); ptr += 1
            needed.append(bulb)
            adj[bulb].append(i)
        
        target = int(input_data[ptr]); ptr += 1
        rule_counts.append(k)
        rule_target.append(target)
    
    # BFS setup
    is_on = [False] * (n + 1)
    queue = deque([1])
    is_on[1] = True
    total_on = 0
    
    while queue:
        u = queue.popleft()
        total_on += 1
        
        # Check every rule that depends on bulb 'u'
        for rule_idx in adj[u]:
            rule_counts[rule_idx] -= 1
            
            # If all conditions for this rule are now met
            if rule_counts[rule_idx] == 0:
                t = rule_target[rule_idx]
                if not is_on[t]:
                    is_on[t] = True
                    queue.append(t)
                    
    print(total_on)

if __name__ == "__main__":
    solve()