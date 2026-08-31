


# get size (S, M, L) and ramen type (R, T)
size, ramen_type = input().split()

# get price table for size x type
prices = {
    'S': { 'R': 60,  'T': 80  },
    'M': { 'R': 80,  'T': 100 },
    'L': { 'R': 100, 'T': 120 }
}

total = prices[ size ][ ramen_type ]

# check for extra toppings
line2 = input().split()
top_char = line2[0]

# if topping is not N (None), add the extra cost
if top_char != 'N':
    count = int( line2[1] )
    per_piece = ( top_char == 'P' ) and 15 or 10
    total += count * per_piece

# show final ramen price
print( total )
