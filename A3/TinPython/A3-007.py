import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    L = int(input_data[0])
    N = int(input_data[1])
    
    # We need to find B such that (B*L * (B*L + 1)) / 2 >= N
    # Let K = B*L
    # K^2 + K - 2N >= 0
    
    # Solve for K using quadratic formula: [-b + sqrt(b^2 - 4ac)] / 2a
    # a=1, b=1, c=-2N
    # K = (-1 + math.sqrt(1 + 8*N)) / 2
    
    required_k = (-1 + math.sqrt(1 + 8 * N)) / 2
    
    # B*L must be at least required_k
    # B >= required_k / L
    
    b = math.ceil(required_k / L)
    
    print(b)

if __name__ == "__main__":
    solve()