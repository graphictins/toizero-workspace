import sys

def solve():
    inventory = {}
    outputs = []
    
    lines = sys.stdin.read().splitlines()
    for line in lines:
        if not line.strip():
            continue
        parts = line.strip().split()
        cmd = parts[0]
        
        if cmd == "ADD":
            name = parts[1]
            qty = int(parts[2])
            inventory[name] = inventory.get(name, 0) + qty
        elif cmd == "REMOVE":
            name = parts[1]
            qty = int(parts[2])
            current = inventory.get(name, 0)
            if qty > current:
                outputs.append(f"Not enough stock for {name}")
                if name in inventory:
                    del inventory[name]
            else:
                inventory[name] -= qty
                if inventory[name] == 0:
                    del inventory[name]
        elif cmd == "CHECK":
            low_stock = [name for name, qty in inventory.items() if qty > 0 and qty < 5]
            if low_stock:
                low_stock.sort()
                outputs.extend(low_stock)
            else:
                outputs.append("All stocks are sufficient")
        elif cmd == "REPORT":
            for name in sorted(inventory.keys()):
                if inventory[name] > 0:
                    outputs.append(f"{name}: {inventory[name]}")
        elif cmd == "END":
            break
            
    for out in outputs:
        print(out)

if __name__ == '__main__':
    solve()
