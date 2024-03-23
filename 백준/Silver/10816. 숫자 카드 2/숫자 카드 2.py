N = int(input())
arr = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))
d = {}
for t in target:
    d[t] = 0
for a in arr:
    if d.get(a) != None:
        d[a] += 1
for t in target:
    print(d[t], end=" ")