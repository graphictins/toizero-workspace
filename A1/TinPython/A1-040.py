

# the table of calories for each order number
calories = {
    1: 100,
    2: 120,
    3: 200,
    4: 60 ,
}

total_calories = 0

# loop forever
while True:
    order = int( input() )
    # if order is 5, break the loop
    if order == 5:
        break
    # if order is not 5
    else:
        # add the calories of the order to the total calories
        total_calories += calories[order]

print("Bye Bye")
print(f"Total Calories: {total_calories}")
