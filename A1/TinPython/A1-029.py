

text = input().strip().lower()

vowels = "aeiou"

vowels_count = 0


for char in text:
    if char in vowels:
        vowels_count += 1

print(vowels_count)
