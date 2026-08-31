

n = int( input() )

min_val = None
 
# loop for ...
for index in range(n):
    num = int( input() )
    # see if new input is more min
    if min_val is None or num < min_val:
        min_val = num

print(min_val)
