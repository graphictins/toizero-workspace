import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    colors = list(map(int, input_data[2:]))

    distinct_count = 0
    color_freq = {}
    ans = 0
    left = 0

    for right in range(n):
        # Add current color to window
        c = colors[right]
        if c not in color_freq or color_freq[c] == 0:
            distinct_count += 1
            color_freq[c] = 1
        else:
            color_freq[c] += 1
        
        # While window is "dazzling", count all subarrays ending from 'right' to 'n-1'
        while distinct_count >= k:
            # If [left, right] is dazzling, then [left, right...n-1] are all dazzling
            ans += (n - right)
            
            # Shrink from left
            left_color = colors[left]
            color_freq[left_color] -= 1
            if color_freq[left_color] == 0:
                distinct_count -= 1
            left += 1

    print(ans)

if __name__ == "__main__":
    solve()