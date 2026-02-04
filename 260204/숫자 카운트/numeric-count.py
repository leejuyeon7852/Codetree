n = int(input())
hints = []
for _ in range(n):
    num, s, b = input().split()
    hints.append((num, int(s), int(b)))

ans = 0 
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i==j or j==k or i==k: # 중복은 안됨
                continue
            candidate = str(i)+str(j)+str(k)
            is_valid = True

            for target_n, target_1, target_2 in hints:
                cnt1 = 0
                cnt2 = 0
                for idx in range(3):
                    if candidate[idx] == target_n[idx]:
                        cnt1 += 1
                    elif candidate[idx] in target_n:
                        cnt2 += 1

                if cnt1 != target_1 or cnt2 != target_2:
                    is_valid = False
                    break
            if is_valid:
                ans += 1

print(ans)

