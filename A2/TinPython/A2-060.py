import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    n = int(data[0])
    bullets = []
    idx = 1
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx+1])
        d = int(data[idx+2])
        bullets.append((x, y, d))
        idx += 3
        
    ans_tx, ans_ty = -1, -1
    for Tx in range(1001):
        for Ty in range(1001):
            valid = True
            for x, y, d in bullets:
                if (Tx - x)**2 + (Ty - y)**2 != d**2:
                    valid = False
                    break
            if valid:
                if ans_tx == -1:
                    ans_tx, ans_ty = Tx, Ty
                else:
                    if Tx < ans_tx or (Tx == ans_tx and Ty < ans_ty):
                        ans_tx, ans_ty = Tx, Ty
                        
    if ans_tx != -1:
        print(f"{ans_tx} {ans_ty}")

if __name__ == '__main__':
    solve()
