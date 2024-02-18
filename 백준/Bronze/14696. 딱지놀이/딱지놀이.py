N = int(input()) #라운드 수
for _ in range(N):
    cntA = [0] * 5
    cntB = [0] * 5
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(1, len(a)):
        cntA[a[i]] += 1
    for j in range(1, len(b)):
        cntB[b[j]] += 1
    if cntA[4] > cntB[4] : print("A")
    elif cntA[4] < cntB[4] : print("B")
    elif cntA[3] > cntB[3] : print("A")
    elif cntA[3] < cntB[3] : print("B")
    elif cntA[2] > cntB[2] : print("A")
    elif cntA[2] < cntB[2] : print("B")
    elif cntA[1] > cntB[1] : print("A")
    elif cntA[1] < cntB[1] : print("B")
    else: print("D")