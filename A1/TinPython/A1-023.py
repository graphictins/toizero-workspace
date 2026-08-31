

temp = int( input() )
unit = input().lower()  # use .lower() to support both lowercase and uppercase

# convert F to C for easier checking
if unit == 'f':
    temp_c = (temp - 32) * 5 / 9
else:
    temp_c = temp

# check state based on temperature in Celsius
if temp_c <= 0:
    print("solid")
elif temp_c >= 100:
    print("gas")
else:
    print("liquid")