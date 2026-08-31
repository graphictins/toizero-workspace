
# make ("12", "345", "3254", "-1234", 0) from "134 435 23 25 3452354 345"
id_cards = input().split(" ")

male   = 0
female = 0


for id_card in id_cards:
    
    id_card = int(id_card)
    
    if id_card < 0:
        
        break
    
    # this thing makes only last digit is left
    last_digit = id_card % 10
    
    # whether this last digit is one of these numbers
    if   last_digit in [1, 3, 5, 7, 9]:
        
        male += 1
    
    # whether this last digit is one of these numbers
    elif last_digit in [0, 2, 4, 6, 8]:
        
        female += 1

print(f"{male} {female} {male + female}")
