import sys
import re

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines: return
    n = int(lines[0].strip())
    
    for i in range(1, n + 1):
        if i >= len(lines): break
        msg = lines[i]
        
        if re.search(r'\b(hello|hi)\b', msg, re.IGNORECASE):
            print("Hello! How can I help you?")
        elif re.search(r'\b(bye|goodbye)\b', msg, re.IGNORECASE):
            print("Goodbye! Have a nice day!")
        elif msg.endswith('?'):
            print("That's an interesting question!")
        elif re.search(r'\d', msg):
            print("I see some numbers there!")
        elif len("".join(msg.split())) > 19:
            print("That's quite a long message!")
        else:
            print("I understand.")

if __name__ == '__main__':
    solve()
