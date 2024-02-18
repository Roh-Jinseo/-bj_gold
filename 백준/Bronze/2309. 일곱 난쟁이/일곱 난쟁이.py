#일곱난쟁이
def seven(t):
    for i in range(9):
        for j in range(i):
            if t - (height[i] + height[j]) == 100 : return i, j

height = []
for _ in range(9):
    height.append(int(input()))
height = sorted(height)
dwa, rfs = seven(sum(height))

for i in range(9):
    if i not in (dwa, rfs): print(height[i])