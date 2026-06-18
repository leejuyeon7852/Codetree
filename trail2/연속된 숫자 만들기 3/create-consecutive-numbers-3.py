arr = list(map(int, input().split()))
arr = sorted(arr)

a, b, c = arr
diff1 = abs(a-b)
diff2 = abs(b-c)

if diff1 == 1 and diff2 == 1:
    print(0)
elif diff1 <= 2 and diff2 <= 2:
    print(1)
else:
    print(max(diff1, diff2)-1)

