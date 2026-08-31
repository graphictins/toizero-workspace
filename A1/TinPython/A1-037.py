

n = int( input() )

# map from large to smol for use case
roman_map = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C') , (90, 'XC') , (50, 'L') , (40, 'XL') ,
    (10, 'X')  , (9, 'IX')  , (5, 'V')  , (4, 'IV')  , (1, 'I')
]

result = ""
# run trought each roman and convert input to new_output(result)
for roman_val, symbol in roman_map:
    # convert value to roman and subtract that roman value
    while n >= roman_val:
        result += symbol
        n -= roman_val

print(result)
