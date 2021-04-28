# Ａ大学は１フロア１０部屋、３階建ての公舎４棟を管理しています。公舎の入居・退去の情報を読み込み、各部屋の入居者数を出力するプログラムを作成して下さい。
# n件の情報が与えられます。各情報では、４つの整数b, f, r, vが与えられます。これは、b棟f階のr番目の部屋にv人が追加で入居したことを示します。vが負の値の場合、-v人退去したことを示します。
# 最初、全ての部屋には誰も入居していないものとします。

# n=int(input())
# give = []
# for i in range(n) :
#     give.append(input())
# c = ['#'*20 if not j%4 else [0 for i in range(1,11)] for j in range(1,16)]
# #print(c)
# for i in range(n) :
#     strList = give[i].split( )
#     b = int(strList[0])
#     f = int(strList[1])
#     r = int(strList[2])
#     v = int(strList[3])
#     c[(b-1)*4+f-1][r-1] += v
# for x in c :
#     print()
#     for y in x :
#         if y =="#":
#             print(y,end='')
#         else :
#             print('', y,end='')



a=[[10*[0]for _ in[0]*3]for _ in[0]*4]
for _ in[0]*int(input()):
    b,f,r,v=map(int,input().split())
    a[b-1][f-1][r-1]+=v
for i in range(4):
    for j in range(3):
        print('',*a[i][j])
    if i<3:print('#'*20)
