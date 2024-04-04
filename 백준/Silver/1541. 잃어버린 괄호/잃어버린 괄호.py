
tk = input()
ans = []
negsum= []
negative = False
s = ''
for t in tk:
    if t.isdigit(): #t가 숫자면
        s += t
    else: #t가 + 또는 -
#         -만나기 전
        if t == '+' and not negative:
            ans.append(int(s))
        # - 바로 직전
        elif t == '-' and not negative:
            ans.append(int(s))
            negative = True

        # - 만난 이후
        else:
            negsum.append(int(s))
        s=''

if negative: negsum.append(int(s))
else: ans.append(int(s))
print(sum(ans) - sum(negsum))