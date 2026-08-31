import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    total_distance = int(input_data[1])
    heights = [int(h) for h in input_data[2:]]
    
    min_mountain_dist = 0
    max_mountain_dist = 0
    
    for h in heights:
        can_be_type1 = (h % 3 == 0)
        can_be_type2 = (h % 4 == 0)
        
        dist1 = (h // 3) * 10 if can_be_type1 else None
        dist2 = (h // 4) * 10 if can_be_type2 else None
        
        if can_be_type1 and can_be_type2:
            # Type 1 distance is always > Type 2 distance for same height
            # 10/3 * h  vs  10/4 * h
            max_mountain_dist += dist1
            min_mountain_dist += dist2
        elif can_be_type1:
            max_mountain_dist += dist1
            min_mountain_dist += dist1
        elif can_be_type2:
            max_mountain_dist += dist2
            min_mountain_dist += dist2
            
    # Flat distance = Total Distance - Mountain Distance
    # Min flat distance comes from Max mountain distance
    ans_min_flat = total_distance - max_mountain_dist
    # Max flat distance comes from Min mountain distance
    ans_max_flat = total_distance - min_mountain_dist
    
    print(f"{ans_min_flat} {ans_max_flat}")

if __name__ == "__main__":
    solve()