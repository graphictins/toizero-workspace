

N = int( input() )
item_list = input().split()
item_list = [ int(item) for item in item_list ]


# sum up all item in item_list
s = sum(item_list)

# count even number in item_list and sum up
#       so 1 for every item in item_list that is even
even = sum(1 for item in item_list if item % 2 == 0)

# count odd number in item_list and sum up
odd  = sum(1 for item in item_list if item % 2 != 0)

print(f"SUM {s}")
print(f"EVEN {even}")
print(f"ODD {odd}")
