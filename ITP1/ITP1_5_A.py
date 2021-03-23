#たてH cm よこ W cm の長方形を描くプログラムを作成して下さい。
#1 cm × 1cm の長方形を '#'で表します。
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print((("#"*b)+"\n")*a) #for i in range(H): print("#"*W) ; print()