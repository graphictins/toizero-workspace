

import sys

# Increase recursion depth just in case of deep nesting
sys.setrecursionlimit(2000)

class Bin:
    def __init__(self, number, Ai, Bi):
        self.number = number
        self.children = []
        self.Ai = Ai
        self.Bi = Bi
        self.total_count = 0
        self.has_target = False

def solve_neutrino():
    # Read from file or stdin
    # input_data = open("A2_input.txt").read().split()
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    it = iter(input_data)
    N = int(next(it))
    M = int(next(it))

    bins_dict = {}
    events = []

    for i in range(1, N + 1):
        x1 = int(next(it))
        x2 = int(next(it))
        # Ensure Ai is always the smaller coordinate
        ai, bi = (x1, x2) if x1 < x2 else (x2, x1)
        bins_dict[i] = Bin(i, ai, bi)
        
        # Tie-breaker: Opening (True) comes before Closing (False) 
        # and Larger bins (smaller Ai, larger Bi) wrap smaller ones
        events.append((ai, -bi, True, i)) 
        events.append((bi, -ai, False, i))

    events.sort()

    stack = []
    roots = []
    # Use a set for actual parent-child tracking to avoid the integer-overwrite issue
    parent_map = {} 

    for _, _, is_opening, bin_num in events:
        if is_opening:
            if stack:
                parent_id = stack[-1]
                bins_dict[parent_id].children.append(bins_dict[bin_num])
                parent_map[bin_num] = parent_id
            else:
                roots.append(bins_dict[bin_num])
            stack.append(bin_num)
        else:
            stack.pop()

    target_bins = []
    for _ in range(M):
        target_bins.append(int(next(it)))
    target_set = set(target_bins)

    def get_stats(node):
        total = 1
        has_t = (node.number in target_set)
        for child in node.children:
            c_total, c_has_t = get_stats(child)
            total += c_total
            has_t = has_t or c_has_t
        node.total_count = total
        node.has_target = has_t
        return total, has_t

    for r in roots:
        get_stats(r)

    memo = {}

    def get_best(node):
        if not node.has_target:
            return 0, 0, []
        if node.number in memo:
            return memo[node.number]

        # Option A: Pick this bin
        res_a = (1, node.total_count, [node.number])

        # Option B: Pick children (only if current isn't a target)
        if node.number not in target_set:
            sum_p, sum_t, all_ids = 0, 0, []
            for child in node.children:
                p, t, ids = get_best(child)
                sum_p += p
                sum_t += t
                all_ids.extend(ids)
            
            if sum_p > 0 and (sum_p < res_a[0] or (sum_p == res_a[0] and sum_t < res_a[1])):
                memo[node.number] = (sum_p, sum_t, all_ids)
                return memo[node.number]

        memo[node.number] = res_a
        return res_a

    final_p, final_t, final_ids = 0, 0, []
    for r in roots:
        p, t, ids = get_best(r)
        final_p += p
        final_ids.extend(ids)

    print(final_p)
    print(*(sorted(final_ids)))

if __name__ == "__main__":
    solve_neutrino()