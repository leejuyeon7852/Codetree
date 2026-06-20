n = int(input())
events = []
for _ in range(n):
    name, delta = input().split()
    delta = int(delta)
    events.append((name, delta))

scores = {'A': 0, 'B': 0, 'C': 0}
prev_top = {'A', 'B', 'C'}  # 명예의 전당
count = 0

for name, delta in events:
    scores[name] += delta

    max_score = max(scores.values())
    current_top = {k for k, v in scores.items() if v == max_score}

    if current_top != prev_top:
        count += 1
        prev_top = current_top

print(count)