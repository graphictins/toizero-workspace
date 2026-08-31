import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    n = int(data[0])
    temps = [float(x) for x in data[1:n+1]]
    
    s = sum(temps)
    avg = s / n
    temps.sort()
    
    if n % 2 != 0:
        med = temps[n//2]
    else:
        med = (temps[n//2 - 1] + temps[n//2]) / 2.0
        
    mx = temps[-1]
    mn = temps[0]
    alert = sum(1 for x in temps if x >= 37)
    
    print(f"SUM={s:.2f}")
    print(f"AVG={avg:.2f}")
    print(f"MEDIAN={med:.2f}")
    print(f"MAX={mx:.2f}")
    print(f"MIN={mn:.2f}")
    print(f"ALERT={alert}")
    print("SORTED=" + " ".join(f"{x:.2f}" for x in temps))

if __name__ == '__main__':
    solve()
