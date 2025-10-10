m = int(input())

if m >= 3 and m <= 5:
    print('Spring')
elif m >= 6 and m <= 8:
    print('Summer')
elif m >= 9 and m <= 11:
    print('Fall')
elif m <= 2 or m >= 12:
    print('Winter')