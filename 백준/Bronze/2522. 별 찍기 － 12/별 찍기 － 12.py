N = int(input())
for i in range(1, N):    print(' '*(N-i) + '*'*(i))
for i in range(N,-1,-1):    print(' ' * (N-i) + '*' * (i))