

units = int( input() )

steps  = [10, 40, 50, 100, 9999]
prices = [5 , 7 , 10, 12 , 15  ]

net_price  = 0
temporary_units = units


# loop through the steps as section 10, 40, 50 for 5, 7, 10
for i in range(5):

    if temporary_units > 0:
        
        # see whats less between temporary_units and one of 10, 40, 50, 100, 9999
        # and take that as what the logic consumed
        consumed   = min(temporary_units, steps[i])
        net_price  += consumed * prices[i]
        temporary_units -= consumed

    else:
        break

FT    = units * 0.50
VAT   = net_price * 0.07
total = net_price + FT + VAT

print(f"{total:.2f}")