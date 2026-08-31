


# get the number of people N
N = int( input() )

# get the list of who sends to who
# target[i] is the person person i sends to
targets = [0] * ( N + 1 )
for i in range( 1, N + 1 ):
    targets[i] = int( input() )

# visitor marks if we have counted a person in a cycle
visited = [False] * ( N + 1 )
max_cycle = 0

# find all cycle lengths
for i in range( 1, N + 1 ):
    if not visited[i]:
        # trace the circle starting from person i
        curr = i
        length = 0
        while not visited[curr]:
            visited[curr] = True
            curr = targets[curr]
            length += 1
        
        # update the biggest circle we found
        if length > max_cycle:
            max_cycle = length

# the game ends when everyone finishes their cycle at least once
# which is just the longest cycle length
print( max_cycle )
