import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    w = int(input_data[0])
    l = int(input_data[1])
    m = int(input_data[2])
    n = int(input_data[3])
    
    min_waste = float('inf')
    total_area = w * l
    
    # Iterate through all possible box lengths A
    # Since N <= 30,000, O(N) is well within 1s limit.
    for a in range(m, n + 1):
        # Phase 1: Boxes along L
        row_capacity = (l // a) * a
        used_p1 = w * row_capacity
        
        # Phase 2: Rotate and fill the remaining strip
        remaining_l = l % a
        col_capacity = (w // a) * a
        used_p2 = remaining_l * col_capacity
        
        current_waste = total_area - (used_p1 + used_p2)
        
        if current_waste < min_waste:
            min_waste = current_waste
            if min_waste == 0: # Optimization: can't get better than 0
                break
                
    print(min_waste)

if __name__ == "__main__":
    solve()