

s = input().strip() # this is needed for this no49 for some reason
d = [ int(x) for x in s ]

floor_numbers = (9, 10, 11, 12, 14)



floor_number = 13
# look up each index , see if greater than 5 then floor_number = what that index floor_number is 9, 10, 11, 12, 14
for i in range(len(d)):
    if d[i] > 5:
        floor_number = floor_numbers[i]
        break



room_1 = 0
if s == s[ : :-1]: # Palindrome

    if   d[0] + d[4] > 5:
        
        room_1 = 1
        
    elif d[1] * d[3] > 5:
        
        room_1 = 2
    
else: # Not a palindrome

    if   d[4] != 0 and d[0] // d[4] > 5:
    
        room_1 = 1
    
    elif d[1] - d[4] > 5:
        
        room_1 = 2



room_2 = 0
if sum(d) > 25:
    
    room_2 = 1

else:

    multiplex = 1
    
    for x in d:
        multiplex *= x
        
    if multiplex > 55:
        room_2 = 2



print(f"{floor_number}{room_1}{room_2}")
