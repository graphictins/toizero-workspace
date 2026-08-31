

n = int( input() )

vowels = "AEIOU"

count = 0

# loop for n times to get input
for index in range(n):
    char = input()
    # see if that input exist in vowels input€vowels
    if char in vowels:
        count += 1

print(count)
