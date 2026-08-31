


# how many holes do we have?
N = int( input() )
points = []

# get all the X and Y coordinates
for _ in range( N ):
    points.append( [ int(x) for x in input().split() ] )

# to make a square, opposite corners must have same (X-Y) or (X+Y)
group1 = {} # for X - Y
group2 = {} # for X + Y

for x, y in points:
    # calculate the "magic numbers" for grouping
    c1 = x - y
    c2 = x + y
    
    # put into groups to find min/max X for each
    if c1 not in group1: group1[c1] = [x, x]
    else:
        group1[c1][0] = min( group1[c1][0], x )
        group1[c1][1] = max( group1[c1][1], x )
        
    if c2 not in group2: group2[c2] = [x, x]
    else:
        group2[c2][0] = min( group2[c2][0], x )
        group2[c2][1] = max( group2[c2][1], x )

max_side = 0

# check all groups to find the biggest square size
for c in group1:
    side = group1[c][1] - group1[c][0]
    if side > max_side: max_side = side

for c in group2:
    side = group2[c][1] - group2[c][0]
    if side > max_side: max_side = side

# show the biggest tent size found
print( max_side )
