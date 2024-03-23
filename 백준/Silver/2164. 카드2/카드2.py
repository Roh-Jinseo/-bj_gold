from collections import deque
N = int(input())
arr = deque(list(range(1,N+1)))
switch = 0
while len(arr)> 1 :
    if switch == 0 :
        arr.popleft()
        switch = 1
    else:
        t = arr.popleft()
        arr.append(t)
        switch = 0
print(*arr)