import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    n = int(data[0])
    p = float(data[1])
    
    idx = 2
    grid = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(int(data[idx]))
            idx += 1
        grid.append(row)
        
    bad_tiles_col = [0] * n
    bad_pts_col = [0] * n
    tot_tiles = 0
    tot_pts = 0
    
    for r in range(n):
        bt_row = sum(1 for x in grid[r] if x > 0)
        bp_row = sum(grid[r])
        tot_tiles += bt_row
        tot_pts += bp_row
        for c in range(n):
            if grid[r][c] > 0:
                bad_tiles_col[c] += 1
            bad_pts_col[c] += grid[r][c]
            
        print(" ".join(map(str, grid[r])) + f" {bt_row} {bp_row}")
        
    print(" ".join(map(str, bad_tiles_col)))
    print(" ".join(map(str, bad_pts_col)))
    fine = tot_pts * p
    print(f"{tot_tiles} {tot_pts} {fine:.2f}")

if __name__ == '__main__':
    solve()
