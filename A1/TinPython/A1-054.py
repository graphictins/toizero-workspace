

texts = input().split()

rank = texts[0]
y = int(texts[1])
s = int(texts[2])

if rank not in ['M', 'B', 'G']:
    print(0)
    exit()

base_bonus_rate = {
    'M': 1500, 
    'B': 1000, 
    'G': 500
}
percent_bonus_rate = {
    'M': (6, 8, 10), 
    'B': (5, 6, 7 ), 
    'G': (4, 5, 6 )
}

year_index = min(2, y // 5)
percent_bonus = percent_bonus_rate[rank][year_index] * s // 100
total_bonus = int(base_bonus_rate[rank] + percent_bonus)

print(total_bonus)
