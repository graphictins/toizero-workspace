

import sys
from decimal import Decimal, ROUND_HALF_UP

def solve():
    # Use a generator to process tokens one by one (memory efficient)
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token
    
    tokens = get_tokens()
    
    is_member = next(tokens, None)
    if is_member is None:
        return
        
    try:
        n = int(next(tokens))
    except (StopIteration, ValueError):
        return

    # sum() with a generator expression is faster and avoids creating list objects
    total = sum((Decimal(next(tokens)) for _ in range(n)), Decimal('0'))

    # Applying the multiplier directly is more efficient than calculating discount then subtracting
    if is_member == 'Y':
        total *= Decimal('0.95')
    elif total >= 500:
        total *= Decimal('0.97')
 
    # Quantize to two decimal places
    print(total.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))

if __name__ == "__main__":
    solve()