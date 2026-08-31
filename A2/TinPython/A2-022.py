
# A2-022: ลอดสะพาน (Under the Bridge)
# Find the vertical cut position that passes under the maximum number of bridges.
# A bridge [A, B] covers a point x strictly: A < x < B (open interval at A and B based on problem).
# We need to check all "event" x positions (midpoints between consecutive bridge endpoints).
# Actually we use a sweep/event approach:
# Collect all unique x-coordinate candidates and count overlaps.

l, n = map(int, input().split())

bridges = []
for _ in range(n):
    a, b = map(int, input().split())
    bridges.append((a, b))

# Candidates: try all values from 0 to L and also midpoints.
# Since bridges are at integer km, a cut at x.5 between integers is optimal.
# We try all half-integer positions: 0.5, 1.5, ..., (L-0.5)
# A bridge [A, B] covers x if A < x < B (strictly).

best = 0
for i in range(l):
    x = i + 0.5
    count = sum(1 for a, b in bridges if a < x < b)
    best = max(best, count)

# Also check if there are integer positions that might be better
for i in range(l + 1):
    x = i
    count = sum(1 for a, b in bridges if a < x < b)
    best = max(best, count)

print(best)
