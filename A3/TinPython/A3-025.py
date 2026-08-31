import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    W = int(input_data[1])
    L = int(input_data[2])
    
    planks_holes = []
    ptr = 3
    for _ in range(N):
        k = int(input_data[ptr])
        holes = [int(x) for x in input_data[ptr+1 : ptr+1+k]]
        planks_holes.append(holes)
        ptr += 1 + k

    # Use the first plank's holes as candidates for the alignment point X.
    # If an alignment exists at point X, then for each plank i, 
    # there must be a hole H_i such that |H_i - X| <= L.
    
    # To optimize, we only need to check X values that are "near" 
    # the holes of the first plank. Specifically, if a solution exists 
    # with some X, then X must be within [H_1 - L, H_1 + L].
    
    # Represent other planks as sets for O(1) lookup
    plank_sets = [set(h) for h in planks_holes]
    
    # Possible alignment points X are H_1 + offset, where offset is [-L, L]
    possible_X = set()
    for h1 in planks_holes[0]:
        for offset in range(-L, L + 1):
            x = h1 + offset
            if 1 <= x <= W:
                possible_X.add(x)
    
    for x in possible_X:
        match_all = True
        for i in range(1, N):
            # For this X, does plank i have a hole H_i in [X-L, X+L]?
            found_hole = False
            for offset in range(-L, L + 1):
                if (x + offset) in plank_sets[i]:
                    found_hole = True
                    break
            if not found_hole:
                match_all = False
                break
        
        if match_all:
            print(1)
            return

    print(0)

if __name__ == "__main__":
    solve()