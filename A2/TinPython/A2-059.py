import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    n = int(data[0])
    d = int(data[1])
    
    names = {
        1: "TechTrends",
        2: "EcoLife",
        3: "FoodieHeaven",
        4: "FashionWeek",
        5: "HealthyLiving"
    }
    
    idx = 2
    top_total = -1
    top_name = ""
    
    for _ in range(n):
        if idx >= len(data): break
        tag_id = int(data[idx])
        idx += 1
        usages = []
        for _ in range(d):
            usages.append(int(data[idx]))
            idx += 1
            
        total = sum(usages)
        avg = total / d
        name = names[tag_id]
        
        if top_total == -1 or total > top_total:
            top_total = total
            top_name = name
            
        first = usages[0]
        last = usages[-1]
        if last > first:
            trend = "GROWING"
        elif last < first:
            trend = "DECLINING"
        else:
            trend = "STABLE"
            
        print(f"{name}: {total} total, {avg:.2f} avg, {trend}")
        
    print(f"Top performer: {top_name}")

if __name__ == '__main__':
    solve()
