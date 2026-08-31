import sys

def solve():
    lines = sys.stdin.read().split()
    if not lines: return
    n = int(lines[0])
    
    students = [f"Student{i}" for i in range(1, n+1)]
    print("Student: " + " ".join(students) if n > 0 else "Student:")
    
    scores = [int(x) for x in lines[1:n+1]] if n > 0 else []
    
    if n > 0:
        highest = max(scores)
        lowest = min(scores)
        avg = sum(scores) / n
    else:
        highest = 0
        lowest = 0
        avg = 0.0
        
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    print(f"Average score: {avg:.1f}")
    print("Students who scored above average:")
    if n > 0:
        for i in range(n):
            if scores[i] > avg:
                print(f"Student {i+1}")

if __name__ == '__main__':
    solve()
