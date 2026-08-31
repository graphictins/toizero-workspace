
n = int(input())
code1 = input().strip()
code2 = input().strip()

bad = 0
for i in range(n):
    if int(code1[i]) + int(code2[i]) != 9:
        bad += 1

if bad == 0:
    print("YES")
else:
    print(f"NO {bad}")
