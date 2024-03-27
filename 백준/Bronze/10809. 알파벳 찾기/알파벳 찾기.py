cnt = [-1]*26
txt = input()
for i in range(len(txt)):
    if cnt[ord(txt[i])-97] == -1 : cnt[ord(txt[i])-97] = i
print(*cnt)