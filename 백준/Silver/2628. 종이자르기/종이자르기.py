width, height = map(int, input().split(" "))
N = int(input())
w = [0, width]
h = [0, height]
for _ in range(N): # cutting
    one, idx = map(int, input().split())
    if one : w.append(idx) # 세로선 자르기 -> 가로 길이가 쪼개짐
    else: h.append(idx) # 가로선 자르기 -> 세로 길리가 쪼개짐
        
w = sorted(w)
h = sorted(h)
maxi = 0
for i in range(len(w)-1):
    for j in range(len(h)-1):
        if abs(w[i+1] - w[i]) * abs(h[j+1]-h[j]) > maxi :
            maxi =  abs(w[i+1] - w[i]) * abs(h[j+1]-h[j])
print(maxi)