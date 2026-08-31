import sys

def solve():
    # Read N and S
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    s = int(input_data[1])
    
    # Store forwarding rules in a dictionary or list
    # forward[i] = the student student i forwards to
    # Using 1-based indexing to match problem description
    forward = [0] * (n + 1)
    for i in range(1, n + 1):
        forward[i] = int(input_data[i + 1])
    
    visited = [False] * (n + 1)
    count = 0
    current = s
    
    # Traverse the path
    while current != 0 and not visited[current]:
        visited[current] = True
        count += 1
        current = forward[current]
        
    print(count)

if __name__ == "__main__":
    solve()