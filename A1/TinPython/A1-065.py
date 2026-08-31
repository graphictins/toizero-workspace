

nums = map(int, input().split())
ans = ""
for n in nums:
    if n == 0:
        ans += "-"
    else:
        s = str(n)
        if len(s) >= 4 and s[-4] > '0':
            ans += "#"
        if len(s) >= 3 and s[-3] > '0':
            ans += "/"
        if len(s) >= 2 and s[-2] > '0':
            ans += "+"
        if len(s) >= 1 and s[-1] > '0':
            ans += "*"
print(ans)
