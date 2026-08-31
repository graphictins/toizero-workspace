

import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

n = int(input_data[0])
score = 0

for i in range(1, 1 + n):
    if i < len(input_data):
        if input_data[i] == '+':
            score += 10
        elif input_data[i] == '-':
            score -= 5

print(score)
