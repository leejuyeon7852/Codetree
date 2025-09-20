# 클래스 선언
class Handshake:
    def __init__(self, t, x, y):
        self.t=t
        self.x=x
        self.y=y
    def __str__(self):
        return f't: {self.t}, x:{self.x}, y:{self.y}'

# 입력
N, K, P, T = map(int, input().split())
handshakes = []
for _ in range(T):
    t, x, y = map(int, input().split())
    handshakes.append(Handshake(t, x, y))

handshakes.sort(key=lambda h: h.t) # 시간 순 정렬

# 감염여부 저장할 list
infected = [0] * (N+1)
infected[P] = 1 # 감염된 개발자 표시

# 악수 횟수 저장할 list
count = [0] * (N+1)

for h in handshakes:
    p1 = h.x
    p2 = h.y
    
    if infected[p1] == 1:
        count[p1] += 1
    if infected[p2] == 1:
        count[p2] += 1
    
    if count[p1] <= K and infected[p1] == 1:
        infected[p2] = 1
    if count[p2] <= K and infected[p2] == 1:
        infected[p1] = 1

# 출력
for i in range(1, N+1):
    print(infected[i], end="")




