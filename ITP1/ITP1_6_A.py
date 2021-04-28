# 与えられた数列を逆順に出力するプログラムを作成して下さい。
# n は数列の長さを示し、ai は i 番目の数を表します。
n=int(input())
testList=list(map(int,input().split()))
testList.reverse()
print((" ").join(str(i) for i in testList))