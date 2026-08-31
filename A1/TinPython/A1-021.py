

year = int( input() )


# check year according to calendar history
if year < 1582:
    # before 1582, just check if divisible by 4
    if year % 4 == 0:
        print("yes")
    else:
        print("no")
else:
    # since 1582, use Gregorian calendar rules
    if ( year % 400 == 0 or year % 4 == 0 ) and not year % 100 == 0:
        print("yes")
    else:
        print("no")