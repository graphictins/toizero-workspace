import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    if n == 0:
        print("0")
        print("0")
        print("0")
    else:
        print(bin(n)[2:])
        print(oct(n)[2:])
        print(hex(n)[2:].upper())

if __name__ == '__main__':
    solve()
