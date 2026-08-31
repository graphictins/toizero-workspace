
# A2-021: รถขนส่ง (Transport Truck)
# Binary search on the answer (max transport time).
# For a given time limit T, greedily count how many items can be produced.
# Each item needs: one A->center route + one center->B route through the SAME center.
# For center 1: pair each A_i->C1 time with each C1->B_j time, sorted ascending.
#   For limit T, count how many pairs (i,j) have a1[i]+b1[j] <= T.
# Total items possible via center 1 = pairs where a1[i]+b1[j] <= T with at most N each used.
# We need at most K items total using both centers (items are distinct pairings).

import bisect

def count_pairs(a_sorted, b_sorted, limit):
    # count pairs (i, j) where a_sorted[i] + b_sorted[j] <= limit
    # each i and j used at most once
    # greedily: sort a ascending, for each a pick the largest b that fits
    count = 0
    right = len(b_sorted) - 1
    for ai in a_sorted:
        # find largest b such that ai + b <= limit
        max_b = limit - ai
        if max_b < 0:
            break
        # binary search in b_sorted
        pos = bisect.bisect_right(b_sorted, max_b) - 1
        if pos >= count:  # at least count+1 b's available means we can pair one more
            # We want to pair greedily: 
            # use the smallest a's with largest valid b's
            pass
        # Actually: sort a ascending, try to match with b descending
        # For each a[i] (ascending), pick the best (largest) unused b that fits
        # This requires a two-pointer approach
    # Use two-pointer: a sorted asc, b sorted desc
    # left pointer on a (start), right pointer on b (start of desc = end of sorted asc)
    count = 0
    j = len(b_sorted) - 1
    for i in range(len(a_sorted)):
        while j >= 0 and a_sorted[i] + b_sorted[j] > limit:
            j -= 1
        if j < 0:
            break
        if j >= i:  # ensure j not already used by a previous a
            count += 1
            j -= 1
        # But this isn't right either since a and b are independent arrays (different trucks)
    return count

def count_items_possible(a1, a2, b1, b2, limit):
    # For center 1: pair a1[i] with b1[j], both <= N trucks, sum <= limit
    # For center 2: pair a2[i] with b2[j], both <= N trucks, sum <= limit
    # We want max items = max matching from center1 + matching from center2
    # where each a-truck used at most once and each b-truck used at most once
    # across both centers combined.
    # Since a-trucks for center1 and center2 are distinct (different routes),
    # and same for b-trucks, we can maximize independently per center.
    
    # For one center: sort a asc, sort b asc, two-pointer to count max pairs
    def max_pairs_one_center(arr_a, arr_b, lim):
        sa = sorted(arr_a)
        sb = sorted(arr_b)
        count = 0
        j = len(sb) - 1
        for i in range(len(sa)):
            if sa[i] > lim:
                break
            # find largest sb[j] such that sa[i] + sb[j] <= lim
            while j >= 0 and sa[i] + sb[j] > lim:
                j -= 1
            if j < 0:
                break
            count += 1
            j -= 1
        return count
    
    c1 = max_pairs_one_center(a1, b1, limit)
    c2 = max_pairs_one_center(a2, b2, limit)
    return c1 + c2

n, k = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
b1 = list(map(int, input().split()))
b2 = list(map(int, input().split()))

# Binary search on answer
lo = 2  # minimum possible sum of two times
hi = 2_000_000

while lo < hi:
    mid = (lo + hi) // 2
    if count_items_possible(a1, a2, b1, b2, mid) >= k:
        hi = mid
    else:
        lo = mid + 1

print(lo)
