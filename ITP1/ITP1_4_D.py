#n 個の整数 ai(i=1,2,...n)を入力し、
# それらの最小値、最大値、合計値を求めるプログラムを作成してください。
a=int(input())
b=list(map(int,input().split()))
print(min(b), max(b), sum(b))

#一番早い書き方：
# _, *a = map(int, open(0).read().split())
# print(min(a), max(a), sum(a))