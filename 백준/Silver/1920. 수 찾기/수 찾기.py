N = int(input())
ns = sorted(list(map(int, input().split())))
mini = ns[0]
maxi = ns[-1]
M = int(input())
ms = list(map(int, input().split()))
# print(N,M,ns,ms)
for i in ms:
    if i < mini or i > maxi : print(0)
    else:
        if i in ns: print(1)
        else: print(0)
