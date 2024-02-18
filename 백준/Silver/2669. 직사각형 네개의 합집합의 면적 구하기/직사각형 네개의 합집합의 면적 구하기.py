N=4
arr = [ [0]*101 for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = list(map(int, input().split()))
    for i in range(x2-x1):
        for j in range(y2-y1):
            arr[x1+i][y1+j] = 1
total = 0
for ar in arr:
    total += sum(ar)
print(total)