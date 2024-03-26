from collections import deque
def inorder(lev, idx):
    if lev == K:
        tree[idx] = arr.popleft()
        return

    inorder(lev+1,idx*2) #L
    tree[idx] = arr.popleft()
    inorder(lev+1,idx*2+1)#R

K = int(input())
arr = deque(list(map(int, input().split())))
tree = [0] + [0]*(2**K-1)
inorder(1, 1)
for i in range(K):    print(*tree[2**i:2**(i+1)])

