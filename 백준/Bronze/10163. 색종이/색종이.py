N = int(input()) #색종이 장 수
space = [ [0] * 1001 for _ in range(1001)]
for order in range(1, N+1):
    x, y, w, h = list(map(int, input().split())) #색종이
    for i in range(w):
        for j in range(h):
            space[x+i][y+j] = order

colored_cnt = [0] * (N+1)
for i in range(1001):
    for j in range(1001):
        colored_cnt[space[i][j]] += 1

for c in range(1,N+1):
    print(colored_cnt[c])