
# A2-025: Rabbit flu outbreak
# Grid of rows x cols (0-indexed)
# N infection sites reported
# Risk zones:
#   - Exact position: 100%
#   - Radius 1 (Chebyshev / Manhattan? - problem says "radius" so we use Chebyshev):
#     cells within distance 1 from any infected cell: 60%
#   - Radius 2: 20%
#   - Otherwise: 0% (safe)
# Overlapping: take the highest risk
# Count safe cells (0%); report rabbit's risk level

rows, cols = map(int, input().split())
rabbit_r, rabbit_c = map(int, input().split())
n_infected = int(input())

infected = []
for _ in range(n_infected):
    r, c = map(int, input().split())
    infected.append((r, c))

# Assign risk to each cell
# Risk: 100, 60, 20, 0
risk_grid = [[0] * cols for _ in range(rows)]

for ir, ic in infected:
    for row in range(rows):
        for col in range(cols):
            dist = max(abs(row - ir), abs(col - ic))  # Chebyshev distance
            if dist == 0:
                r_level = 100
            elif dist == 1:
                r_level = 60
            elif dist == 2:
                r_level = 20
            else:
                r_level = 0
            risk_grid[row][col] = max(risk_grid[row][col], r_level)

safe_count = sum(1 for row in range(rows) for col in range(cols) if risk_grid[row][col] == 0)
rabbit_risk = risk_grid[rabbit_r][rabbit_c]

print(safe_count)
print(f"{rabbit_risk}%")
