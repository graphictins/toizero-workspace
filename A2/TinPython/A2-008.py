


# how many car models are there?
N = int( input() )

scores = []
# get price and performance for each model
for _ in range( N ):
    # prices are already sorted 100, 90, 80... we only need the scores
    p, v = map( int, input().split() )
    scores.append( v )

# we check from the cheapest car (the end of the list)
unsellable_count = 0
max_so_far = -1

# loop backwards from the last car to the first
for i in range( N - 1, -1, -1 ):
    # if this car is better than all cheaper cars, it can be sold!
    if scores[i] > max_so_far:
        max_so_far = scores[i]
    else:
        # if there exists a cheaper car that is better, this one is useless
        unsellable_count += 1

# show how many cars nobody will buy
print( unsellable_count )
