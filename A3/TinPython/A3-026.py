import sys

def solve():
    # Read all input and split into tokens
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    # Grid 1: Rows from index 2 to N+1
    grid1 = input_data[2 : 2 + N]
    
    # Grid 2: Rows from index N+2 to 2N+1
    grid2 = input_data[2 + N : 2 + 2 * N]
    
    result = []
    
    for r in range(N):
        row_output = []
        for c in range(M):
            char1 = grid1[r][c]
            char2 = grid2[r][c]
            
            # Application of overlay logic
            if char1 == '-' and char2 == '-':
                row_output.append('-')
            elif (char1 == '+' and char2 == 'x') or (char1 == 'x' and char2 == '+'):
                row_output.append('*')
            elif char1 == '+' or char2 == '+':
                # If one is '+' and the other isn't 'x', result is '+'
                row_output.append('+')
            elif char1 == 'x' or char2 == 'x':
                # If one is 'x' and the other isn't '+', result is 'x'
                row_output.append('x')
            else:
                # Fallback for unexpected characters
                row_output.append(char1)
                
        result.append("".join(row_output))
    
    # Print final combined image
    print("\n".join(result))

if __name__ == "__main__":
    solve()