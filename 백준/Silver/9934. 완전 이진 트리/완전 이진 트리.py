def preorder(lev, s,e):
    if lev == K:        return
    tree[lev].append(arr[(s+e)//2])#V
    preorder(lev+1,s, (s+e)//2-1) #L
    preorder(lev+1,(s+e)//2+1, e)#R

K = int(input())
arr = list(map(int, input().split()))
tree = [ [] for _ in range(K) ]
preorder(0,0, len(arr))
for t in tree:    print(*t)