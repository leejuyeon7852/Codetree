N = int(input())
seat = input()

people = [i for i in range(N) if seat[i] == "1"] # 0, 4, 7, 12
empty = [i for i in range(N) if seat[i] == "0"] # 1, 2, 3, 5, 6, 8, 9, 10, 11, 13

ans = 0
for i in range(len(empty)):
    for j in range(i+1, len(empty)):
        placed = sorted(people + [empty[i], empty[j]])
        min_dist = min(placed[k+1]-placed[k] for k in range(len(placed)-1))
        ans = max(ans, min_dist)

print(ans)