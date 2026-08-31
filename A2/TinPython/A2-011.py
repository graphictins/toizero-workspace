


# get 10 numbers from the input
nums = input().split()
unique_nums = []

# loop through each number to check for duplicates
for n in nums:
    # if we haven't seen this number yet, save it
    if n not in unique_nums:
        unique_nums.append( n )

# show the unique numbers in a single line
print( " ".join( unique_nums ) )
