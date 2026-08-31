import sys

def intersects(u1, v1, u2, v2, n):
    # If they share a segment, they meet
    if {u1, v1} == {u2, v2}:
        return True
    
    # If they share a stop, they don't meet 'between' stops (per problem rules)
    if len({u1, v1, u2, v2}) < 4:
        return False
        
    # Normalize points so u1 is the reference (0)
    # Positions are relative to u1 clockwise
    a, b, c = (v1-u1)%n, (u2-u1)%n, (v2-u1)%n
    
    # Chord 1 is [0, a]. Chord 2 is [b, c].
    # They intersect if one point of Chord 2 is inside (0, a) 
    # and the other is outside (a, n).
    if (0 < b < a and (c < 0 or c > a)) or (0 < c < a and (b < 0 or b > a)):
        return True
    
    return False

def solve():
    data = sys.stdin.read().split()
    if not data: return
    
    n = int(data[0])
    red = [1] + [int(x) for x in data[1:n+1]]
    blue = [1] + [int(x) for x in data[n+1:2*n+1]]
    
    meets = 0
    for i in range(n):
        if intersects(red[i], red[i+1], blue[i], blue[i+1], n):
            meets += 1
            
    print(meets)

if __name__ == "__main__":
    solve()