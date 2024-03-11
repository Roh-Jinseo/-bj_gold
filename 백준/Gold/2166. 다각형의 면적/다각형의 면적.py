N = int(input())
xs = []
ys = []
for _ in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
xs = xs + [xs[0]] #x_n+1 = x_0
ys = ys + [ys[0]] #y_n+1 = y_0
A = 0
for i in range(N):
    A += xs[i]*ys[i+1] - xs[i+1]*ys[i]
print(abs(round(A/2,1)))