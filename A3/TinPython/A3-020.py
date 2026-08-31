import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    h1, h2, b1, b2 = map(int, input_data[:4])
    x, y = map(int, input_data[4:])
    
    max_profit = 0
    
    # Iterate through all possible counts of White-White robots (w)
    # h1 and b1 are small (<= 100), so O(N) is perfect.
    for w in range(min(h1, b1) + 1):
        # 1. Matching color robots
        # White-White: w
        # Black-Black: The leftover black heads and black bodies
        left_h2 = h2 - (b1 - w)
        left_b2 = b2 - (h1 - w)
        
        # Ensure we don't have negative parts
        if left_h2 < 0 or left_b2 < 0:
            continue
            
        black_black = min(left_h2, left_b2)
        k = w + black_black
        
        # 2. Different color robots
        # White Head + Black Body: h1 - w
        # Black Head + White Body: b1 - w
        l = (h1 - w) + (b1 - w)
        
        # Total profit for this configuration
        current_profit = min(k, x) + min(l, y)
        max_profit = max(max_profit, current_profit)
        
    print(max_profit)

if __name__ == "__main__":
    solve()