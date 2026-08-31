

s, e = map( int, input().split() )
# create a list of numbers
numbers = [ x for x in range(s, e + 1) ]

primes = []



# prime numbers are never even-number
odds = [ x for x in numbers if x % 2 == 1 ]

# prime numbers are never one that sums of digits are divisible by 3
# ... lazy

# manual cleanup
if 1 in odds:

    odds.remove(1)

if 2 in numbers:

    odds.insert(0, 2)



# loop through each number in odds
for x in odds:
    # loop through each number from 2 to square root of x
    for y in range(2, int(x ** 0.5 + 1)):
        # if x is divisible by y, then it is not prime
        if x % y == 0:
            break
    # if x is not divisible by any of y, then it is prime
    else:
        primes.append(x)



output = ""

for prime in primes: 

    output += f"{prime} "

output.strip()

print(output)

print(f"Total primes: {len(primes)}")