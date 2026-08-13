def yangsu(num, arr):
    if num in arr:
        return yangsu(num+1, arr)
    else:
        return num

T = int(input())
cases = []
for _ in range(T):
    cases.append(int(input()))

Length = max(cases)+1
sanbul = [0]*Length
sanbul[0] = 1
sanbul[1] = 1
for i in range(2, Length):
    localmax = []
    for k in range(1, int(i/2)+1):
        if (2*sanbul[i-k] - sanbul[i-2*k]) > 0:
            localmax.append(2*sanbul[i-k] - sanbul[i-2*k])
    sanbul[i] = yangsu(1, localmax)
for j in cases:
    print(sanbul[j])