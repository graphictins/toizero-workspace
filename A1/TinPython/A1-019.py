

a = int( input() )
b = int( input() )
c = int( input() )

# check if all numbers are the same
if a == b and b == c:
    print("all the same")

# check if all numbers are different
elif a != b and b != c and a != c:
    print("all different")

# the rest (some numbers are the same but not all)
else:
    print("neither")