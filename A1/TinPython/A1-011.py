

string = input()

count = 1
output = ""

# loop through each index based on lenght of string
for index in range( len(string) ):
    # check if next index exist, and if next index is same as current index
    if index + 1 < len(string) and string[index] == string[index+1]:
        count += 1
    else:
        # add count and current index to output
        output += str(count) + string[index]
        # reset count to 1
        count = 1

print(output)