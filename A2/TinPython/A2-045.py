import sys
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    blocks = []
    for i in range(0, len(input_data), 2):
        prev = int(input_data[i])
        curr = int(input_data[i+1])
        blocks.append((prev, curr))
        if curr == 0:
            break
            
    if len(blocks) == 1:
        print("1X")
        return
        
    def check_blocks(idx):
        if idx == len(blocks) - 1:
            return
        
        check_blocks(idx + 1)
        
        status = 'P' if blocks[idx][1] == blocks[idx+1][0] else 'X'
        print(f"{idx+1}{status}")
        
    check_blocks(0)

if __name__ == '__main__':
    solve()
