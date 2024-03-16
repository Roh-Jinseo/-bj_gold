def check():
    #row check
    for row in range(5):
        if hor[row] == 0 and sum(called[row])==5:
            hor[row] = 1

    for col in range(5):
        if ver[col] == 0 :
            for col in range(5):
                c = 0
                for row in range(5):
                    c += called[row][col]
                if c == 5 : ver[col] = 1
    if diag[0] == 0 :
        d0 = 0
        for i in range(5): d0 += called[i][i]
        if d0 == 5 : diag[0] = 1
    if diag[1] == 0 :
        d1 = 0
        for i in range(5): d1 += called[i][4-i]
        if d1 == 5: diag[1] = 1
    if sum(diag + ver + hor )>=3: return True

mine = [ list(map(int, input().split())) for _ in range(5)]
calls = []
for _ in range(5):
    calls.extend(list(map(int, input().split())))
called = [ [0]*5 for _ in range(5)]
ver, hor, diag = [0]*5, [0]*5, [0,0]
cnt = 0
for call in calls:
    for i in range(5):
        for j in range(5):
            if mine[i][j] == call:
                called[i][j] = 1
                cnt += 1
    if cnt >= 12:
        if check():
            print(cnt)
            break