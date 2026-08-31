import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    q = int(input_data[1])
    
    # Pre-calculate the span of the river at each depth
    # depth_spans[h] = [min_x, max_x] for that depth level
    # Since the river starts and ends at depth 0 (ground),
    # and depth is always > 0 in between:
    
    left_bound = {}  # First time we reach depth h
    right_bound = {} # Last time we are at depth h
    
    curr_x = 0
    curr_h = 0
    
    pointer = 2
    for _ in range(n):
        d = int(input_data[pointer])
        l = int(input_data[pointer+1])
        
        if d == 1:
            # Going deeper: The "left" boundary for the new depth is the current X
            curr_h += 1
            if curr_h not in left_bound:
                left_bound[curr_h] = curr_x
        else:
            # Going shallower: The "right" boundary for the current depth is the current X + L
            if curr_h not in right_bound or (curr_x + l) > right_bound[curr_h]:
                right_bound[curr_h] = curr_x + l
            curr_h -= 1
            
        curr_x += l
        pointer += 2

    max_depth = max(left_bound.keys())
    # total_width[h] is the continuous distance between 
    # the first time we hit h and the last time we leave h.
    max_len_at_depth = [0] * (max_depth + 1)
    
    for h in range(1, max_depth + 1):
        if h in left_bound and h in right_bound:
            max_len_at_depth[h] = right_bound[h] - left_bound[h]

    # Ensure monotonicity: if you fit at depth h+1, you fit at depth h
    for h in range(max_depth - 1, 0, -1):
        if max_len_at_depth[h+1] > max_len_at_depth[h]:
            max_len_at_depth[h] = max_len_at_depth[h+1]

    # Answer queries using binary search
    results = []
    for _ in range(q):
        w = int(input_data[pointer])
        pointer += 1
        
        # Find the largest h such that max_len_at_depth[h] >= w
        low = 1
        high = max_depth
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if max_len_at_depth[mid] >= w:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        results.append(str(ans))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()