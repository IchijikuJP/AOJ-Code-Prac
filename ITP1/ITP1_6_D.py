# n×m の行列 A と、m×1 の列ベクトルb を読み込み、A と b の積を出力するプログラムを作成してください。
n,m=map(int,input().split())
A=[input().split()for _ in[0]*n]
b=[input()for _ in[0]*m]
for a in A:
    print(sum(int(x)*int(y)for x,y in zip(a,b)))
print(A,b)