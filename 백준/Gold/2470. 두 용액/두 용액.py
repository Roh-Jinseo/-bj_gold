N = int(input())
nums = list(map(int, input().split()))
nums.sort()
h, t = 0, N-1
mini = 9876554321
mini_pair=0
while h != t:
    if abs(nums[h] + nums[t]) < mini:
        mini = abs(nums[h] + nums[t])
        mini_pair = (nums[h],nums[t])
    if nums[h] + nums[t] > 0 :        t -= 1
    elif nums[h] + nums[t] < 0:        h += 1
    else:        break

print(*mini_pair)