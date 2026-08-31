

g = int( input().strip() )
r = int( input().strip() )

if g < 1 or g > 6 or r < 1 or r > 6:
    print("Invalid")
elif g == r:
    print("Correct!")
else:
    print("Wrong!")
