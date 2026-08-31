import sys

def solve():
    # Read input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # Convert prices to integers
    prices = list(map(int, input_data[1:]))
    
    # Use a set to store unique sums
    unique_sums = set()
    
    # Iterate through every possible starting restaurant 'i'
    for i in range(n):
        current_sum = 0
        # For each start, iterate through every possible ending restaurant 'j'
        for j in range(i, n):
            current_sum += prices[j]
            unique_sums.add(current_sum)
            
    # The answer is the number of elements in the set
    print(len(unique_sums))

if __name__ == "__main__":
    solve()