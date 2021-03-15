#３つの整数a, b, cを読み込み、それらが a < b < cの条件を満たすならば"Yes"を、
# 満たさないならば"No"を出力するプログラムを作成して下さい。
a, b, c = map(int, input().split())
if(a<b<c):
    print("Yes")
else:
    print("No")
# a=1;b=2;c=3
# print(a,b,c)
# print(a<b<c)