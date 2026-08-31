

seasons = [ 
    "winter",
    "spring",
    "summer",
    "fall"  ,
]

# the variable "month" is now a season selector "and not month it self"
month, day = int( input() ), int( input() )


if day >= 21 and month % 3 != 0:
    month += 1

print(seasons[month - 1])