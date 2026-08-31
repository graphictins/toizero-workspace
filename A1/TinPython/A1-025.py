

s = input().strip().lower()

# Split components: Rank is index 0 to and stop before -1, Suit is always last
rank_part = s[:-1]
suit_char = s[-1]

# Table 1: Ranks (Face cards + Ace)
rank_map = {
    'a': 'ace',
    'j': 'jack',
    'q': 'queen',
    'k': 'king'
}

# Table 2: Suits
suit_map = {
    'd': 'diamonds',
    'h': 'hearts',
    's': 'spades',
    'c': 'clubs'
}

# if rank_part is a key in rank_map, use that value; otherwise, use rank_part as is.
if rank_part in rank_map:
    rank_name = rank_map[rank_part]
else:
    rank_name = rank_part

# Direct Lookup for Suit
suit_name = suit_map[suit_char]

# Output formatting
print(f"{rank_name} of {suit_name}")