#２つの整数 x, y を読み込み、それらを値が小さい順に出力するプログラムを作成して下さい。
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print("%d %d" % (a,b) if a<=b else  ("%d %d" % (b,a)))  #三元运算符
        