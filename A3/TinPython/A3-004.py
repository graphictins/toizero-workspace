import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    u_coords = []
    v_coords = []
    
    idx = 1
    for _ in range(n):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        u_coords.append(x + y)
        v_coords.append(x - y)
        idx += 2
        
    # Sort to find medians and calculate sum of deviations
    u_coords.sort()
    v_coords.sort()
    
    # The median is the optimal point. 
    # For sum of |x_i - median|, the formula is:
    # Sum_{i=0 to n-1} (u[i] * (2i - n + 1))
    
    def min_total_dist(sorted_list):
        size = len(sorted_list)
        median = sorted_list[size // 2]
        return sum(abs(val - median) for val in sorted_list)

    ans = min_total_dist(u_coords) + min_total_dist(v_coords)
    print(int(ans))

if __name__ == "__main__":
    solve()