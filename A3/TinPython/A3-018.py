import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    l = int(input_data[0])
    n = int(input_data[1])
    
    # We remove oranges from the top (Layer 1, then Layer 2, etc.)
    # We need to find how many layers are affected by removing N oranges.
    
    layers_removed = 0
    oranges_to_remove = n
    
    # Iterate from the top layer (i=1) to the bottom layer (i=L)
    for i in range(1, l + 1):
        if oranges_to_remove <= 0:
            break
            
        # Number of oranges in the current top-most layer
        layer_size = i * i
        
        # Subtract the layer size from the remaining removal quota
        oranges_to_remove -= layer_size
        layers_removed += 1
        
    # Remaining layers = Total - Removed
    print(l - layers_removed)

if __name__ == "__main__":
    solve()