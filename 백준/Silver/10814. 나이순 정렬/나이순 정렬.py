N = int(input())
l = [ (input().split()) for _ in range(N)]
l.sort(key = lambda x : int(x[0]))
for a in l:
    print(*a)