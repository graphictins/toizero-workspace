import sys

def solve():
    # Efficiently read input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # Tasks are the remaining N integers
    tasks = list(map(int, input_data[1:]))
    
    overtime_count = 0
    normal_count = 0
    
    # Categorize tasks
    for h in tasks:
        if h > 18:
            overtime_count += 1
        else:
            normal_count += 1
            
    # Every Overtime Task needs a 'recovery slot' on the next day.
    # We prioritize using Normal Tasks as recovery slots.
    
    # Cases:
    # 1. More Normal Tasks than Overtime Tasks:
    #    We can alternate O, N, O, N... and then finish remaining N.
    #    Total days = overtime_count + normal_count = N.
    if normal_count >= overtime_count:
        print(n)
    
    # 2. More Overtime Tasks than Normal Tasks:
    #    We use all normal_count tasks to buffer overtime_count tasks.
    #    Remaining Overtime Tasks = overtime_count - normal_count.
    #    Each of these remaining tasks requires 1 day to work + 1 day to rest.
    #    Except for the very last task (if it's the last thing you ever do).
    else:
        # Initial days spent on pairs and remaining normals
        # (O, N) pairs take 2 * normal_count days
        # Remaining O tasks = (overtime_count - normal_count)
        
        extra_o = overtime_count - normal_count
        # Pattern: O, N, O, N ... O, Rest, O, Rest ... O
        # Each extra_o (except the last) takes 2 days. The last takes 1.
        total_days = (2 * normal_count) + (2 * extra_o) - 1
        print(total_days)

if __name__ == "__main__":
    solve()