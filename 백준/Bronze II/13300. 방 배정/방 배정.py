T, K = map(int, input().split())
arr = [ [0]*(2) for _ in range(6+1)]
room_num = 0
for _ in range(T):
    gender, grade = map(int, input().split())
    arr[grade][gender] += 1

for i in range(1, 7):
    for j in arr[i]:
        room_num += j//2 + j%2
print(room_num)