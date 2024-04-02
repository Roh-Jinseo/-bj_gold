N, K = map(int, input().split())
ks = []
for _ in range(N):    ks.append(int(input()))
cnt = 0
idx = N -1
while True:
    if ks[idx] > K :
        idx -= 1
    else: #ks[idx] <= K
        if K > 0 :
            s,r = divmod(K, ks[idx])
            cnt += s
            K = r
            if K == 0 :
                print(cnt)
                break