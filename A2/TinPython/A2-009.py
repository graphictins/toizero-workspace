


# get the number of teams N and the team with the special card C
line1 = input().split()
N = int( line1[0] )
C = int( line1[1] )

# get the winning table (results[i][j] is the winner between i and j)
results = [ [] for _ in range( N + 1 ) ]
for i in range( 1, N + 1 ):
    # each line i has N results for team i
    row = [ int(x) for x in input().split() ]
    results[i] = [0] + row

# teams is a list of [team_id, card_available]
teams = []
for i in range( 1, N + 1 ):
    # only team C has a card (True)
    has_card = ( i == C )
    teams.append( [ i, has_card ] )

# simulate each round until only 1 team is left
while len( teams ) > 1:
    next_round = []
    # pair them up: matching team 0 with 1, 2 with 3, etc.
    for i in range( 0, len( teams ), 2 ):
        t1 = teams[i]
        t2 = teams[i+1]
        
        # see who wins naturally
        winner_id = results[ t1[0] ][ t2[0] ]
        
        # card logic: if someone is about to lose but has the card
        if winner_id == t2[0] and t1[1]:
            # force t1 to win and burn the card
            next_round.append( [ t1[0], False ] )
        elif winner_id == t1[0] and t2[1]:
            # force t2 to win and burn the card
            next_round.append( [ t2[0], False ] )
        else:
            # natural winner proceeds, card status stays same
            winner = t1 if winner_id == t1[0] else t2
            next_round.append( winner )
            
    teams = next_round

# show the final champion
print( teams[0][0] )
