


# how many trees are there?
N = int( input() )
# get heights of all trees
H = [ int(x) for x in input().split() ]

count = 0

# loop through each tree and check its neighbors
for i in range( N ):
    is_best = True
    
    # if there is a tree on the left, it must be shorter
    if i > 0:
        if H[i-1] > H[i]: is_best = False
        
    # if there is a tree on the right, it must be shorter too
    if i < N - 1:
        if H[i+1] > H[i]: is_best = False
        
    # if both neighbors are shorter, nappy bird is happy!
    if is_best:
        count += 1

# show how many trees the birds like
print( count )
