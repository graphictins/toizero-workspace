


# get width, length and number of layers for the fence
w, l, n = map( int, input().split() )
# get how much 1 meter of wire costs
price = int( input() )

# calculate the length of one layer (perimeter)
one_layer = 2 * ( w + l )

# calculate total wire for all layers
total_wire = one_layer * n

# calculate final price
total_cost = total_wire * price

# show wire length first, then the money needed
print( total_wire )
print( total_cost )
