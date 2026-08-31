

import math

x1, y1, z1 = map(float, input().split())
x2, y2, z2 = map(float, input().split())

# using formula to find distance of two 3d points
d = math.sqrt( 0 # zero doesn't count just for beautiful code
    + (x2 - x1) ** 2 
    + (y2 - y1) ** 2 
    + (z2 - z1) ** 2 
)

print(f"{d:.2f}")
