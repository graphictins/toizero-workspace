

# how many pairs
n = int( input() )
# all numbers
nums = input().strip().split()

max_values = []


for i in range(n):

    A = int( nums[i * 2] )
    B = int( nums[i * 2 + 1] )
    max_values.append(max(A, B))

total_sum = sum(max_values)

if n == 1:

    print(max_values[0])
    
else:

    # build equation
    equation = f"{max_values[0]}"
    # list number in the list starting from index 1
    for value in max_values[1:]:
        equation += f" + {value}"

    print(f"{equation} = {total_sum}")