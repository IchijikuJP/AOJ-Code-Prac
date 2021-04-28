#トランプ : 不足しているカードの発見
n=int(input())
pokerCheck = []
for i in range(n) :
    pokerCheck.append(input())
def init(): #初始化一套完整扑克牌
    pokers=[]
    for i in ['S','H','C','D']:
        for j in ['1','2','3','4','5','6','7','8','9','10','11','12','13']:
            pokers.append(i+' '+j)
    return pokers
pokerFull=init()

c = []
for i in range(len(pokerFull)) :
    if not (pokerFull[i] in pokerCheck) :
        c.append(pokerFull[i])

print(("\n").join(str(i) for i in c))

# 一番早い書き方
c=[f'{s} {i}'for s in'SHCD'for i in range(1,14)]    #格式化字符串f-string (py3.6以上)
for _ in[0]*int(input()):c.remove(input())
for x in c:print(x)