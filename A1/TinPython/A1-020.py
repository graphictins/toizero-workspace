

a = int( input() )
b = int( input() )
c = int( input() )

# check if strictly increasing
if a < b and b < c:
    print("increasing")

# check if strictly decreasing
elif a > b and b > c:
    print("decreasing")

# the rest (e.g. 3 4 4 or 5 2 8)
else:
    print("neither")