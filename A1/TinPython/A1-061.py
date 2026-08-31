

r, x, y = map( int, input().split() )

# determinds the distance without squareroot because out put is only IN, ON, OUT
# this line just r squared to match the un-squareroot distance
r2 = r * r
# this line is finding distance using phytagorean theorem without squareroot
d2 = x * x + y * y

if d2 < r2:
    print("IN")
elif d2 == r2:
    print("ON")
else:
    print("OUT")
