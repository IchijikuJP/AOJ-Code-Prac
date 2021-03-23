#３つの整数 a、b、c を読み込み、a から b までの整数の中に、
# c の約数がいくつあるかを求めるプログラムを作成してください。
a, b, c = map(int, input().split())
i = a
cnt = 0
for i in range(a,b+1) :
    if (c%i == 0): 
        cnt += 1 
    # print("约数为 %d, 余数为 %d" % (i, 80%i))
    # print("当前共有 %d 个约数" % cnt)
print(cnt)

