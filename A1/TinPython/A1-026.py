

nums = [
    int( input() ),
    int( input() ),
    int( input() ),
]

even_count = 0

for num in nums:
    if num % 2 == 0:
        even_count += 1

odd_count = 3 - even_count

print(f"even {even_count}")
print(f"odd {odd_count}")
