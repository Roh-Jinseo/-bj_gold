N = int(input())
arr = list(map(int, input().split()))
new = []
for i in range(N):
    new.insert(i-arr[i], i+1)
print(*new)
