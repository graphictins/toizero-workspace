


# get winning ticket prefix and number
win_pref, win_num = input().split()
# get customer's prefix and number
my_pref, my_num = input().split()

prize = 0

# check exact match for 1,000,000
if win_pref == my_pref and win_num == my_num:
    prize = 1000000
# check 5 digits match but prefix doesn't
elif win_num == my_num:
    prize = 100000
# check last 3 digits and prefix
elif win_pref == my_pref and win_num[-3:] == my_num[-3:]:
    prize = 2000
# check last 2 digits and prefix
elif win_pref == my_pref and win_num[-2:] == my_num[-2:]:
    prize = 1000
# check last 3 digits only
elif win_num[-3:] == my_num[-3:]:
    prize = 200
# check last 2 digits only
elif win_num[-2:] == my_num[-2:]:
    prize = 100
# check prefix match only
elif win_pref == my_pref:
    prize = 20

# show how much money we won
print( prize )
