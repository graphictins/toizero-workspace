

n = int( input() )

fact = 1


# loop start from 1 to n stop before n+1 and step by 1
for i in range(1, n + 1):
    fact *= i

print(fact)
