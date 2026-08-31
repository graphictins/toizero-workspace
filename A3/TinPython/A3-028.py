import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # Parse dimensions and mine count
    N = int(input_data[0])
    M = int(input_data[1])
    num_mines = int(input_data[2])
    
    # Initialize grid with zeros
    # Using a list of lists for O(1) coordinate access
    grid = [[0 for _ in range(M)] for _ in range(N)]
    mine_positions = []
    
    # Track mine locations
    idx = 3
    for _ in range(num_mines):
        r = int(input_data[idx])
        c = int(input_data[idx + 1])
        grid[r][c] = 'x'
        mine_positions.append((r, c))
        idx += 2
        
    # Relative coordinates for 8 neighbors
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    # Calculate adjacency counts
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 'x':
                continue
            
            count = 0
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                # Check if neighbor is within bounds and is a mine
                if 0 <= nr < N and 0 <= nc < M:
                    if grid[nr][nc] == 'x':
                        count += 1
            grid[r][c] = str(count)
            
    # Output the grid with space separation
    for row in grid:
        print(" ".join(row))

if __name__ == "__main__":
    solve()