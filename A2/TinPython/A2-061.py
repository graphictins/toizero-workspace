

import sys

def solve():
    # 1. Initialize Teams and Matches
    teams = ["CHE", "LIV", "MUN", "NEW"]
    points = {team: 0 for team in teams}
    
    # Pre-defined match order based on problem logic (i < j)
    matches = [
        ("CHE", "LIV"), ("CHE", "MUN"), ("CHE", "NEW"),
        ("LIV", "MUN"), ("LIV", "NEW"), ("MUN", "NEW")
    ]

    # 2. Process 6 match results
    for i in range(6):
        try:
            line = sys.stdin.readline().split()
            if not line: break
            score_a, score_b = map(int, line)
            
            team_a, team_b = matches[i]
            
            if score_a > score_b:
                points[team_a] += 3
            elif score_b > score_a:
                points[team_b] += 3
            else:
                points[team_a] += 1
                points[team_b] += 1
        except ValueError:
            continue

    # 3. Sort Results: Primary (Points desc), Secondary (Name asc)
    # Python's sort is stable; we sort by name first, then points.
    # Alternatively, use a key with -points for descending.
    sorted_standings = sorted(points.items(), key=lambda x: (-x[1], x[0]))

    # 4. Output
    for idx, (name, pts) in enumerate(sorted_standings, 1):
        print(f"{idx}. {name} {pts}")

if __name__ == "__main__":
    solve()