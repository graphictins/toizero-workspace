import sys

def solve():
    # Use fast I/O for large M (up to 100,000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    events = []
    idx = 2
    for _ in range(m):
        s = int(input_data[idx])
        t = int(input_data[idx+1])
        # Entry event: +1
        # Exit event: -1 (at T+1 because T is inclusive)
        events.append((s, 1))
        events.append((t + 1, -1))
        idx += 2
        
    # Sort events by coordinate
    # If coordinates are the same, the -1 will naturally process 
    # after +1 if we just sort tuples.
    events.sort()
    
    max_clique = 0
    current_overlap = 0
    
    for _, type in events:
        current_overlap += type
        if current_overlap > max_clique:
            max_clique = current_overlap
            
    print(max_clique)

if __name__ == "__main__":
    solve()