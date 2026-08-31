


# get the size of the grid N
N = int( input() )
grid = []
for _ in range( N ):
    grid.append( input() )

# reachable[r][c] will be True if we can go to the finish from here
# initialize all to False
reachable = [ [False] * N for _ in range( N ) ]

# start checking from the bottom-right corner (the goal!)
if grid[N-1][N-1] == '.':
    reachable[N-1][N-1] = True

# loop backwards from bottom to top
for r in range( N-1, -1, -1 ):
    # loop backwards from right to left
    for c in range( N-1, -1, -1 ):
        # already checked the goal
        if r == N-1 and c == N-1:
            continue
            
        # if this cell is a rock, we can't be here
        if grid[r][c] == 'X':
            continue
            
        # can reach goal if we can go DOWN to a good cell
        can_go_down  = ( r + 1 < N and reachable[r+1][c] )
        # or if we can go RIGHT to a good cell
        can_go_right = ( c + 1 < N and reachable[r][c+1] )
        
        if can_go_down or can_go_right:
            reachable[r][c] = True

count = 0
# count all the starting spots that can reach the goal
for r in range( N ):
    for c in range( N ):
        if reachable[r][c]:
            count += 1

# show how many good spots we found
print( count )
