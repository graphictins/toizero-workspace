

# n = int(input())

# print(f"{n:,}")

n = input().strip()[::-1]


water_baby_count = (len(n) - 1) // 3

# character at the front where no need to do anything
char_left_count  = (len(n) - 1) % 3 + 1
char_left        = n[ -char_left_count: ]

new_text = ""

# add "000," to text block by block  ---> 000, + 000, + ...
for i in range(water_baby_count):
    new_text += n[ i * 3:(i + 1) * 3 ] + ","

# add the character at the front     ---> 000, + 001
new_text += char_left
# reverse the text                   ---> 100, + 000,
new_text = new_text[::-1]
# yay                                ---> 100,000
print(new_text)
