N, K = map(int, input().split())
arr = list(map(int, input().split()))
x = sum(arr[:K])
h, t = 0, K
maxi = x
for i in range(N-K):
    x = x - arr[h] + arr[t]
    if x > maxi : maxi = x
    h += 1
    t += 1
print(maxi)