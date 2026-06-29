A = input()

def encoding(A):
    arr = []
    curr_ch = A[0]
    count = 1
    for i in range(1, len(A)):
        if A[i] == curr_ch:
            count += 1
        else:
            arr.append(str(count)+curr_ch)
            curr_ch = A[i]
            count = 1
    arr.append(str(count)+curr_ch)
    result = "".join(arr)
    #print(result)
    return len(result)

min_len = 99999
for i in range(len(A)):
    if i == 0: 
        shifted_A = A
    else:
        shifted_A = A[-i:]+A[:-i]
    
    min_len = min(min_len, encoding(shifted_A))

print(min_len)