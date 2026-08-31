

amount = int( input() )

# loop trought each coin value
for coin in [10, 5, 2, 1] :

    # get the most amount this coin is used  exp: 35$ use 3 of coin10
    used_coins = amount // coin

    # get the remainder                      exp: 35$ use 3 of coin10. now we have 5$ left
    amount %= coin

    print(f"{coin} = {used_coins}")

