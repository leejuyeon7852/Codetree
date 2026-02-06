n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

area = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            
            if x1 == x2:
                height = abs(y1-y2)
                if y3 == y2:
                    width = abs(x2-x3)
                    area = max(area, height*width)
                if y3 == y1:
                    width = abs(x1-x3)
                    area = max(area, height*width)
            if x2 == x3:
                height = abs(y2-y3)
                if y1 == y2:
                    width = abs(x1-x2)
                    area = max(area, height*width)
                if y1 == y3:
                    width = abs(x1-x3)
                    area = max(area, height*width)
            if x1 == x3:
                height = abs(y1-y3)
                if y2 == y3:
                    width = abs(x2-x3)
                    area = max(area, height*width)
                if y2 == y1:
                    area = max(area, height * abs(x2 - x1))

print(area)
                

            

             