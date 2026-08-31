import sys

def solve():
    # Read input: N people, K step size, T thief's number
    line = sys.stdin.readline()
    if not line:
        return
    
    parts = list(map(int, line.split()))
    if len(parts) < 3:
        return
    
    n, k, t = parts
    
    # Convert to 0-indexing for easier modulo math
    # Person 1 -> index 0
    # Person T -> index t-1
    start_pos = 0
    thief_pos = t - 1
    
    current_pos = start_pos
    count = 1 # Person 1 always considers the gift first
    
    # Limit simulation to N steps (gift must return to 1 or hit T within N steps)
    for _ in range(n):
        # Move gift by K steps
        current_pos = (current_pos + k) % n
        
        # Condition 1: Returns to Person 1 (index 0)
        if current_pos == start_pos:
            break
            
        # Condition 2: Reaches the Thief
        count += 1
        if current_pos == thief_pos:
            break
            
    print(count)

if __name__ == "__main__":
    solve()