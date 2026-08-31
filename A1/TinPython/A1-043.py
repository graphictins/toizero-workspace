

import math

base  = int( input() )
bonus = int( input() )
days  = int( input() )

# table of if total_score >= key then value
rank = (
    (1500, 5),
    (1000, 4),
    (500 , 3),
    (200 , 2),
    (0   , 1),
)


# total_score = if days <= 3  then base + bonus  else ( base + bonus ) * 1.5
total_score = ( days <= 3 ) and ( base + bonus ) or int( ( base + bonus ) * 1.5 )

# find rank
for key, value in rank:
    if total_score >= key:
        rank = value
        break

special_status = 0

if   rank == 5 and days >= 7:
    special_status = 99
elif rank == 4 and bonus > 300:
    special_status = 88

print(total_score)
print(rank)
print(special_status)
