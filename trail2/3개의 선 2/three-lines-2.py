n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

def check(points, lines):
    if not points:
        return True
    if lines == 0:
        return False  
    
    x0, y0 = points[0]
    
    remaining = [p for p in points if p[0] != x0]
    if check(remaining, lines - 1):
        return True
    
    remaining = [p for p in points if p[1] != y0]
    if check(remaining, lines - 1):
        return True
    
    return False

print("1" if check(points, 3) else "0")