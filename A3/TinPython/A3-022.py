import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    # Track segments: track[i] represents the interval [i, i+1]
    track = [False] * 360
    
    idx = 1
    for _ in range(N):
        A = int(input_data[idx])
        B = int(input_data[idx + 1])
        idx += 2
        
        if A < B:
            # Normal interval
            for i in range(A, B):
                track[i] = True
        else:
            # Circular interval wrapping around 0
            for i in range(A, 360):
                track[i] = True
            for i in range(0, B):
                track[i] = True
                
    # Check if fully covered
    if all(track):
        print(360)
        return

    # Find longest continuous lit sequence
    # Double the track to easily handle circular sequences
    extended_track = track + track
    max_duration = 0
    current_duration = 0
    
    for lit in extended_track:
        if lit:
            current_duration += 1
            if current_duration > max_duration:
                max_duration = current_duration
        else:
            current_duration = 0
            
    # Result cannot exceed 360
    print(min(max_duration, 360))

if __name__ == "__main__":
    solve()