

import math

room = int(input())

if room == 1:
    print(0)
else:
    floor = math.ceil(math.sqrt(room))
    
    # Your original parity logic:
    # If they match (Even/Even or Odd/Odd), it's +2. 
    # If they don't match, it's +1. 
    travel = 2 if (floor % 2 == room % 2) else 1
    
    # Your original mid_section logic
    travel += (floor - 2) * 2
    
    print(travel)