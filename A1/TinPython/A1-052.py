

n = int( input().strip() )

# either out of range or have remainder will the error be shown
if n < 100 or n > 20000 or (n % 100 != 0):
    print("ERROR")
else:
    count_1000 = n // 1000
    n %= 1000
    
    count_500 = n // 500
    n %= 500
    
    count_100 = n // 100
    
    if count_1000 > 0:
        print(f"1000 = {count_1000}")
    if count_500 > 0:
        print(f"500 = {count_500}")
    if count_100 > 0:
        print(f"100 = {count_100}")
