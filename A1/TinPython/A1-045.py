

# nothing to explain
dist = int( input() )


if dist == 0:
    fare = 35
elif dist <= 1:
    fare = 35
elif dist <= 10:
    fare = 35 + (dist - 1) * 5
else:
    fare = 35 + 9 * 5 + (dist - 10) * 8

print(fare)
