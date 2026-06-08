N = int(input())
str = input()

min_length = N

for L in range(1, N+1):
    substrings = set()
    for i in range(N-L+1):
        substrings.add(str[i:i+L])
    if len(substrings) == N-L+1:
        print(L)
        break

#print(min_length)
        
        
