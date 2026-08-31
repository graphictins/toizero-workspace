

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

class Segment:
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1
    
    def __repr__(self):
        return f"Segment[{self.p0} -> {self.p1}]"

class Beam:
    def __init__(self, event_points):
        self.event_points = event_points
        self.segment_index = 0
        self.segments = []
        
        current_y = 1
        for x in self.event_points:
            # Logic remains identical
            start_x = 0 if not self.segments else self.segments[-1].p1.x
            point0 = Point(start_x, current_y)
            
            next_y = 1 if current_y == 0 else 0
            point1 = Point(x, next_y)

            self.segments.append(Segment(point0, point1))
            current_y = next_y


def main():
    
    # red_N, blue_M = 5, 7
    # red_hit_points  = [ 2, 7, 8, 15, 20 ]
    # blue_hit_points = [ 3, 4, 5, 7, 10, 16, 21 ]
    
    # red_N, blue_M = 2, 4
    # red_hit_points  = [ 10, 20 ]
    # blue_hit_points = [ 5, 10, 15, 20 ]
    
    # red_N, blue_M = 4, 8
    # red_hit_points  = [ 10, 20, 30, 40 ]
    # blue_hit_points = [ 5, 10, 15, 20, 25, 30, 35, 40 ]
    
    # red_N, blue_M = 2, 4
    # red_hit_points  = [10, 20]
    # blue_hit_points = [5, 15, 25, 35]


    
    red_N, blue_M = map( int, input().strip().split() )

    red_hit_points  = list( map( int, input().strip().split() ) )
    blue_hit_points = list( map( int, input().strip().split() ) )

        
        
    red  = Beam(event_points=red_hit_points)
    blue = Beam(event_points=blue_hit_points)

    
    event_points = sorted(set(red_hit_points + blue_hit_points))


    intersections = []

    for seg in red.segments:
        for seg2 in blue.segments:
            inter = line_intersection(seg, seg2) 
            if inter and inter.y >= 0 and inter.y <= 1:
                intersections.append( (inter.x, inter.y) )
    
    
    intersec_count = len( sorted(list(set(intersections))) )
    print(intersec_count)
    

def line_intersection(seg1: Segment, seg2: Segment):
    
    # Ax + By = C form for both lines blablabla
    A1 = seg1.p1.y - seg1.p0.y
    B1 = seg1.p0.x - seg1.p1.x
    C1 = A1 * seg1.p0.x + B1 * seg1.p0.y

    A2 = seg2.p1.y - seg2.p0.y
    B2 = seg2.p0.x - seg2.p1.x
    C2 = A2 * seg2.p0.x + B2 * seg2.p0.y

    denominator = A1 * B2 - A2 * B1
    if denominator == 0:
        return None  # Lines are parallel

    return Point(
        x = (B2 * C1 - B1 * C2) / denominator,
        y = - (C1 * A2 - C2 * A1) / denominator
    )


main()