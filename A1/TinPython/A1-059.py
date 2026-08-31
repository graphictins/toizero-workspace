

route = input().strip()

weight = int( input().strip() )

# table of base fee and per_kg_fee for each route
fees = {
    "BKK CNX": (10, 30),
    "CNX UBP": (15, 40),
    "UBP BKK": (20, 40),
    "BKK PKT": (25, 50),
    "PKT CNX": (30, 60),
    "UBP PKT": (40, 70)
}


if route in fees:
    
    # use the fees by that route
    base_fee, per_kg_fee = fees[route]
    
    total = base_fee + weight * per_kg_fee
    
    print(total)
    
else:
    
    print("Error")
