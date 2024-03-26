N = int(input())
for _ in range(N):
    token = input()
    t = -1 ; ans = True
    for tk in token:
        if tk == '(': t += 1
        elif tk ==')' and t >= 0 : t -= 1
        else:   ans = False ;  break
    if t > -1 : ans = False
    print("YES") if ans else print("NO")