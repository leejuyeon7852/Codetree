n = int(input())
rounds = []
for _ in range(n):
    a, b, c = map(int, input().split())
    rounds.append((a, b, c))

max_score = 0

for start in [1, 2, 3]:
    stone = start
    score = 0
    for a, b, c in rounds:
        if stone == a:
            stone = b
        elif stone == b:
            stone = a
        
        if stone == c:
            score += 1
    max_score = max(max_score, score)

print(max_score)


        
