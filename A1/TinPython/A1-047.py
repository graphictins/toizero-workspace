

N = int(input().strip())
A = int(input().strip())

if N == 0 or A == 0:
    print("No teaching")

else:
    total_min = N * A
    hour = total_min // 60
    minute = total_min % 60

    hour_text   = ( hour   == 1) and f"{hour} hour"     or f"{hour} hours"
    minute_text = ( minute == 1) and f"{minute} minute" or f"{minute} minutes"

    if hour > 0 and minute > 0:
        print(f"{hour_text} {minute_text}")
    elif hour > 0:
        print(f"{hour_text}")
    else:
        print(f"{minute_text}")
