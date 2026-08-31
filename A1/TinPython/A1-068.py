

n = int(input())
scores = list(map(int, input().split()))
avg = sum(scores) / n

print(f"{avg:.1f}")

all_pass = True
for s in scores:
    if s < 50:
        all_pass = False

if avg >= 60.0 and all_pass:
    print("PASS")
else:
    print("FAIL")
