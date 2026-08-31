


# how many bowls to clean?
N = int( input() )

# use a dictionary to count how many of each size we have
counts = {}

for _ in range( N ):
    size = int( input() )
    # add 1 to the count for this size
    if size not in counts: counts[size] = 1
    else: counts[size] += 1

max_piles = 0

# the number of piles needed is just the frequency of the most common bowl
for s in counts:
    if counts[s] > max_piles:
        max_piles = counts[s]

# show the smallest number of piles needed
print( max_piles )
