import sys

def solve():
    # Efficiently read input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # Extract pole lengths and sort ascending to minimize total distance
    lengths = sorted([int(x) for x in input_data[1:]])
    
    total_distance = 0
    current_prefix_sum = 0
    
    for length in lengths:
        current_prefix_sum += length
        # Round trip to the current pole's tip
        total_distance += 2 * current_prefix_sum
        
    print(total_distance)

if __name__ == "__main__":
    solve()