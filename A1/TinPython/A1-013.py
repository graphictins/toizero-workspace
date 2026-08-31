

char_input = input()
num_input  = int( input() )

PASSCHAR = "H"
PASSCODE = 4567

if char_input == PASSCHAR and num_input == PASSCODE:
    print("safe unlocked")
    
elif char_input == PASSCHAR:
    print("safe locked - change digit")
    
elif num_input == PASSCODE:
    print("safe locked - change char")
    
else:
    print("safe locked")