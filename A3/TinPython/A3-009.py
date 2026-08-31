import sys

def solve():
    # Read all input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    # row_counts[i] stores how many people have joined row (i+1)
    row_counts = [0] * k
    
    # Process each passenger's row assignment
    for i in range(2, len(input_data)):
        row_id = int(input_data[i])
        # row_id is 1-indexed, map to 0-indexed
        row_counts[row_id - 1] += 1
        
    # The number of full sets (pods) that could have left
    # is limited by the row with the fewest people.
    num_pods = min(row_counts)
    
    # Total people remaining = Total entered - (Total departed)
    # Total departed = number of pods * capacity K
    remaining = n - (num_pods * k)
    
    print(remaining)

if __name__ == "__main__":
    solve()