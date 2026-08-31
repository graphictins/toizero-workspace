


# get bread size W, H and number of cuts M, N
line1 = input().split()
W = int( line1[0] )
H = int( line1[1] )
M = int( line1[2] )
N = int( line1[3] )

# get vertical cuts and add edges 0 and W
x_cuts = [0] + [ int(x) for x in input().split() ] + [W]
# get horizontal cuts and add edges 0 and H
y_cuts = [0] + [ int(y) for y in input().split() ] + [H]

# find all widths and heights of the small pieces
widths  = []
for i in range( len(x_cuts) - 1 ):
    widths.append( x_cuts[i+1] - x_cuts[i] )

heights = []
for i in range( len(y_cuts) - 1 ):
    heights.append( y_cuts[i+1] - y_cuts[i] )

# multiply widths and heights to find all areas
areas = []
for w in widths:
    for h in heights:
        areas.append( w * h )

# sort all areas from big to small
areas.sort( reverse=True )

# show the top two biggest areas
print( f"{areas[0]} {areas[1]}" )
