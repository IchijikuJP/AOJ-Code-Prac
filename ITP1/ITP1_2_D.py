#長方形の中に円が含まれるかを判定するプログラムを作成してください。
#次のように、長方形は左下の頂点を原点とし、右上の頂点の座標 (W,H) が与えられます。
#また、円はその中心の座標 (x,y) と半径 r で与えられます。

W, H, x, y ,r = map(int, input().split())
if(2*r > x+r or x+r>W or 2*r>y+r or y+r>H):
    print("No")
else :
    print("Yes")

# 一番早い書き方：print("Yes"*(r<=x<=W-r)*(r<=y<=H-r)or"No")