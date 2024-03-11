import math
def find_kth():
    cnt = 0
    for i in range(2, N + 1):
        kth = i
        for j in range(1, N // i + 1):
            kth = i * j
            if kth <= N and arr[kth]:
                cnt += 1
                arr[kth] = 0
            if cnt == K:
                print(kth)
                return

N, K = map(int, input().split())
arr = [1] * (N+1) #0,1, 2~N
find_kth()