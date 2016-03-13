def Zeros(N):
    a,p=0,5
    while p <= N:
        a += N/p
        p *= 5
    return a