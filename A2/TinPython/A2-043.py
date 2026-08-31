import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])
    cave = [int(x) for x in input_data[1:n+1]]
    moves = input_data[n+1]
    
    pos = cave.index(1)
    cave[pos] = 0
    
    for move in moves:
        nxt = pos
        if move == 'L':
            nxt -= 1
        elif move == 'R':
            nxt += 1
            
        if 0 <= nxt < n:
            if cave[nxt] == 2:
                pos = nxt
                break
            else:
                pos = nxt
    
    cave[pos] = 1
    print(" ".join(map(str, cave)))

if __name__ == '__main__':
    solve()
