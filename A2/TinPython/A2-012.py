


# carrot = 10, cabbage = 25, tomato = 3
prices = [ 10, 25, 3 ]

# get how many of each item rabbit bought
items = [ int(x) for x in input().split() ]

total = 0
# multiply each item count by its price
for i in range( 3 ):
    total += items[i] * prices[i]

# show the final total price
print( total )
