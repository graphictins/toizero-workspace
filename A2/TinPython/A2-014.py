import sys

def solve():
    # Read names and remove extra whitespace
    lines = sys.stdin.read().split()
    if len(lines) < 2:
        return
    
    name1 = lines[0]
    name2 = lines[1]
    
    # Stage 1: Length Normalization
    len1, len2 = len(name1), len(name2)
    if len1 < len2:
        name1 += (name1[0] * (len2 - len1))
    elif len2 < len1:
        name2 += (name2[0] * (len1 - len2))
    
    # Stage 2: Character Transformation
    love = {'l', 'o', 'v', 'e'}
    yantra_list = []
    
    for c1, c2 in zip(name1, name2):
        if c1.lower() in love or c2.lower() in love:
            yantra_list.append('w')
        else:
            yantra_list.append('$')
            
    yantra = "".join(yantra_list)
    
    # Stage 3: Final Ritual
    w_count = yantra.count('w')
    
    # Calculate max consecutive w and check for pairs
    max_consecutive_w = 0
    current_consecutive = 0
    has_pair = False
    
    for char in yantra:
        if char == 'w':
            current_consecutive += 1
            if current_consecutive >= 2:
                has_pair = True
        else:
            max_consecutive_w = max(max_consecutive_w, current_consecutive)
            current_consecutive = 0
    max_consecutive_w = max(max_consecutive_w, current_consecutive)
    
    if w_count % 2 != 0:
        # Odd count: append max consecutive length
        print(f"{yantra}{max_consecutive_w}")
    else:
        # Even count
        if not has_pair and w_count > 0:
            # If no w-pairs exist and there were actually w's
            print(f"{yantra}#")
        elif w_count == 0 and not has_pair:
            # Special case: 0 is even, but no pairs exist
            print(f"{yantra}#")
        else:
            print(yantra)

if __name__ == "__main__":
    solve()