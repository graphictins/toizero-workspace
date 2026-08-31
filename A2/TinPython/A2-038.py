
n = int(input())

fire_total = 0
water_total = 0
earth_total = 0

for _ in range(n):
    f1, w1, e1, f2, w2, e2 = map(int, input().split())
    sum1 = f1 + w1 + e1
    sum2 = f2 + w2 + e2
    if sum1 >= sum2:
        fire_total += f1
        water_total += w1
        earth_total += e1
    else:
        fire_total += f2
        water_total += w2
        earth_total += e2

total = fire_total + water_total + earth_total
print(total)
print(fire_total, water_total, earth_total)
if fire_total > water_total + earth_total:
    print("YES")
else:
    print("NO")
