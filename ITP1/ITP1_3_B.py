#１つの整数 x を読み込み、それをそのまま出力するプログラムを作成して下さい。
#python 3读取未知多行输入

case_num = 1

while True:
    tmp_num = int(input())
    if tmp_num == 0:
        break
    else:
        print("Case %d: %d" % (case_num,tmp_num))
        case_num += 1
