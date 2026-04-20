N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

max_total = 0

def get_amount(temp,ta, tb):
    if temp < ta:
        return C
    elif ta <= temp <= tb:
        return G
    else:
        return H

candidates = [0]
for ta, tb in ranges:
    candidates.append(ta)
    candidates.append(tb)
    candidates.append(tb + 1)
    
for temp in sorted(set(candidates)):
    total = sum(get_amount(temp, ta, tb) for ta, tb in ranges)
    if total > max_total:
        max_total = total

print(max_total)

