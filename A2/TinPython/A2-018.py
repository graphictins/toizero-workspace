


# get start color R, G, B and total count N
line = input().split()
start = line[0]
N     = int( line[1] )

# set the cycling order
order = [ 'Red', 'Green', 'Blue' ]

# find where we start in the circle
if   start == 'R': idx = 0
elif start == 'G': idx = 1
else:              idx = 2

res = []
# loop N times to build the sequence
for _ in range( N ):
    # add the current color name to our list
    res.append( order[ idx ] )
    # go to next color (wrap around to 0 if at the end)
    idx = ( idx + 1 ) % 3

# show the colors joined by space
print( " ".join( res ) )
