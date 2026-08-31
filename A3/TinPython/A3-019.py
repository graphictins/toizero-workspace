import sys

def solve():
    # Read all input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    l = int(input_data[1])
    
    # Heights of all N people
    heights = list(map(int, input_data[2:2+n]))
    
    # Indices of the L customers (1-based from input)
    # Convert to 0-based for list indexing
    customer_indices = [int(x) - 1 for x in input_data[2+n:]]
    
    # Precompute prefix maximums or just iterate
    # Since L is small and indices are sorted, 
    # we can do it in one pass.
    
    current_max = -1
    height_ptr = 0
    
    for target_idx in customer_indices:
        # Update current_max to include everyone BEFORE the current customer
        while height_ptr < target_idx:
            if heights[height_ptr] > current_max:
                current_max = heights[height_ptr]
            height_ptr += 1
        
        # Calculate chair height
        # Customer height is heights[target_idx]
        if current_max < heights[target_idx]:
            print(0)
        else:
            # Need to be max + 1
            print(current_max - heights[target_idx] + 1)
        
        # Note: We do NOT update current_max with the customer's 
        # own height yet because the next customer needs to look
        # at this customer's ORIGINAL height (per problem rules).
        if heights[target_idx] > current_max:
            current_max = heights[target_idx]
        height_ptr = target_idx + 1

if __name__ == "__main__":
    solve()