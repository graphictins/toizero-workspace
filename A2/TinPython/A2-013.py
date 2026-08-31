


# get topping type and its weight in grams
line1 = input().split()
top_type = line1[0]
top_gram = int( line1[1] )

# get tea type, sweetness level, and volume in cc
line2 = input().split()
tea_type = line2[0]
sweet    = int( line2[1] )
volume   = int( line2[2] )

# set topping calorie rates
top_rates = { 'H': 5, 'O': 3, 'J': 2 }
# set tea calorie rates based on [level 1, level 2, level 3]
tea_rates = {
    'R': [ 12, 18, 25 ],
    'T': [ 15, 20, 30 ],
    'M': [ 10, 15, 20 ]
}

# calculate calorie for topping part
cal_top = top_rates[ top_type ] * top_gram

# calculate calorie for tea part
# sweet - 1 because list index starts at 0
cal_tea = tea_rates[ tea_type ][ sweet - 1 ] * volume

# show the total calorie count
print( cal_top + cal_tea )
