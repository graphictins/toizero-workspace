import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    A = int(input_data[0])
    B = int(input_data[1])
    
    N = B - A + 1
    max_sum = 3 * B
    
    # 1. Sieve of Eratosthenes
    is_prime = [True] * (max_sum + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(max_sum**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, max_sum + 1, p):
                is_prime[i] = False
    
    # 2. Count frequencies of sums x + y + z where A <= x <= y <= z <= B
    # To count sets (order doesn't matter), we use the formula based on 
    # permutations of (x, y, z):
    # Total = (Ways All Distinct + 3 * Ways 2 Same + Ways 3 Same) / 6 is NOT applicable here.
    # We use a generating function approach or simpler:
    
    # Let f[s] be the number of ways to pick 1 element from [A, B] to get sum s.
    # Here, f[s] = 1 for s in [A, B], else 0.
    
    # Let count1(s) = ways to pick 1 element from [A, B] to get sum s
    # Let count2(s) = ways to pick 2 elements (order matters) to get sum s
    # Let count3(s) = ways to pick 3 elements (order matters) to get sum s
    
    # To find unique sets (unordered):
    # Let S1 = sum_{i} x_i (where x_i in [A, B])
    # Let S2 = sum_{i} x_i^2
    # Let S3 = sum_{i} x_i^3
    
    # Using Newton's Sums / Combinatorial Generating Functions:
    # Let P(z) = z^A + z^{A+1} + ... + z^B
    # We want coefficient of z^prime in (P(z)^3 + 3*P(z)*P(z^2) + 2*P(z^3)) / 6
    
    limit = 3 * B
    p1 = [0] * (limit + 1)
    for i in range(A, B + 1): p1[i] = 1
        
    p2 = [0] * (limit + 1)
    for i in range(A, B + 1):
        if 2 * i <= limit: p2[2 * i] = 1
            
    p3 = [0] * (limit + 1)
    for i in range(A, B + 1):
        if 3 * i <= limit: p3[3 * i] = 1
            
    # Calculate P(z)^2
    p1_sq = [0] * (limit + 1)
    for i in range(A, B + 1):
        for j in range(A, B + 1):
            if i + j <= limit:
                p1_sq[i + j] += 1
                
    # Calculate P(z)^3
    p1_cu = [0] * (limit + 1)
    # Optimization: iterate only over non-zero indices
    p1_sq_indices = [i for i, val in enumerate(p1_sq) if val > 0]
    for i in p1_sq_indices:
        for j in range(A, B + 1):
            if i + j <= limit:
                p1_cu[i + j] += p1_sq[i]
                
    # Calculate 3 * P(z) * P(z^2)
    p1p2 = [0] * (limit + 1)
    p2_indices = [i for i, val in enumerate(p2) if val > 0]
    for i in p2_indices:
        for j in range(A, B + 1):
            if i + j <= limit:
                p1p2[i + j] += 3 * p1[j]

    total_sets = 0
    for s in range(3 * A, 3 * B + 1):
        if is_prime[s]:
            # Apply Polya Enumeration / Generating Function for Multisets of size 3
            ways = (p1_cu[s] + p1p2[s] + 2 * p3[s]) // 6
            total_sets += ways
            
    print(total_sets)

solve()