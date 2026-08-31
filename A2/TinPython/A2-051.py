import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    try:
        n = int(data[0])
        m = int(data[1])
    except:
        return
        
    if not (1 <= n <= 10 and 1 <= m <= 20):
        print("Data Incorrect")
        return
        
    idx = 2
    total_score = 0
    for i in range(1, n + 1):
        team_scores = []
        for j in range(m):
            if idx < len(data):
                team_scores.append(int(data[idx]))
                idx += 1
        
        avg = sum(team_scores) / len(team_scores) if team_scores else 0
        mx = max(team_scores) if team_scores else 0
        total_score += sum(team_scores)
        
        print(f"Team {i}: Average = {avg:.2f}, Max = {mx}")
        
    print(f"Total Score of All Teams = {total_score}")

if __name__ == '__main__':
    solve()
