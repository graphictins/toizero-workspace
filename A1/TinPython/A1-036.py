

n = int( input() )

output = ""

# loop start from n to 0 stop before -1 and step by -1
for i in range(n, -1, -1):
    # whether this num is multiple of 10
    if i % 10 == 0:
        # add that num to output  ---> "" + "10 " + "20 "
        output += f"{i} "

print(output)
