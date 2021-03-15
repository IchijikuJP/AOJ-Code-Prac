#３つの整数を読み込み、それらを値が小さい順に並べて出力するプログラムを作成して下さい。
testList= list(map(int, input().split()))
# print(testList)
testList.sort()
print((" ").join(str(i) for i in testList))