import sys

def solve():
    # Read input using fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    # Construct the grid from the flat token list
    grid = []
    idx = 2
    for r in range(N):
        row = input_data[idx : idx + M]
        grid.append(row)
        idx += M
        
    # Create a copy for the next hour's state
    # We use list comprehension to avoid reference issues
    next_grid = [row[:] for row in grid]
    
    # Process flow logic
    # Row 0 stays the same as it has no "above"
    for r in range(1, N):
        for c in range(M):
            # If the cell directly above was flooded in the current hour
            if grid[r-1][c] == '*':
                next_grid[r][c] = '*'
                
    # Output the result with space separation
    for row in next_grid:
        print(" ".join(row))

if __name__ == "__main__":
    solve()