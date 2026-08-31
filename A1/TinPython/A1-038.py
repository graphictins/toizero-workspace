

n = int( input() )

result = ""

# loop start from 1 to n stop before n+1 and step by 1
for i in range(1, n + 1):
    # whether this num is multiple of 5
    if i % 5 == 0:
        # add "X" to result
        result += "X"
    else:
        # add "*" to result
        result += "*"

print(result)
