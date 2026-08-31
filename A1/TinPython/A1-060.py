

r, h, g = map( float, input().split() )
pi      = 3.14

width = h + 2 * r
length = 2 * pi * r + g

print(f"{width:.2f} {length:.2f}")
