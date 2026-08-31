

s = input().strip().lower()
k = int( input().strip() )

# table of alphabet so character can shift index
alphabet = "abcdefghijklmnopqrstuvwxyz"

# output holder
caesar_cipher = ""

for character in s:
    # find index of that character
    index = alphabet.find(character)
    # shift index by k value with in range of 26
    new_index = (index + k) % 26
    # add new character in that new index to caesar_cipher
    caesar_cipher = caesar_cipher + alphabet[new_index]

print(caesar_cipher)