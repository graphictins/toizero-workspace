


score1 = int(input())
score2 = int(input())
score3 = int(input())

is_pass = "pass"


# if any of scores dont pass 50% of its max score, the whole thing fails
if score1 < 5 or score2 < 20 or score3 < 25 :
    is_pass = "fail"

print(is_pass)


