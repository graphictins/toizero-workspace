

# get input and split into two variables by space
age, day = input().split()
age = int(age)

# 19 up
if age >= 19:
    price = 150
# 5 to 18
elif age >= 5:
    price = 100
# 0 to 4
else:
    price = 0

if day == "Wed":
    price = int(price / 2)

print(price)
