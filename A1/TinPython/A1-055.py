

a, b, c = map( int, input().split() )

cost  = a * 25 + b * 40 + c * 55
items = a + b + c

if items >= 3:
    cost = int(cost * 0.9)
else:
    cost = int(cost)
    
print(cost)
