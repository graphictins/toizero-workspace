

import sys

def solve():
    # Reading input string
    try:
        line = sys.stdin.readline()
        if not line:
            return
        text = line.strip()
    except EOFError:
        return

    # Define target vowels and initialize counts
    vowels = ['a', 'e', 'i', 'o', 'u']
    counts = {v: 0 for v in vowels}

    # Single pass iteration: O(n)
    for char in text.lower():
        if char in counts:
            counts[char] += 1

    # Filter and display: O(1) (fixed size 5)
    for v in vowels:
        if counts[v] > 0:
            print(f"{v}: {counts[v]}")

if __name__ == "__main__":
    solve()