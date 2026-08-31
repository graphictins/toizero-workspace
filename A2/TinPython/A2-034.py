
import math

n = int(input())

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.isqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

if is_prime(n):
    print("Yes")
    primes = [str(p) for p in range(2, n + 1) if is_prime(p)]
    print(' '.join(primes))
else:
    print("No")
