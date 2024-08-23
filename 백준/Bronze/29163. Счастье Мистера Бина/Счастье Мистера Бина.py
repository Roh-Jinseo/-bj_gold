n = int(input())
arr = list(map(int, input().split(" ")))
even, odd = 0, 0
for i in arr:
    if i % 2 == 0: even += 1
    else: odd += 1
if even > odd : print("Happy")
else: print("Sad")