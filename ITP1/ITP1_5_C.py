while True:
    a,b=map(int,input().split())
    if a==0 and b==0:break
    f=[[0 for i in range(b)]for j in range(a)]
    for i in range(a):
        for j in range(b):
            if (i+j)%2== 0:
                f[i][j]=1
    for i in range(a):
        for j in range(b):
            if f[i][j]==1:
                print('#',end='')
            else :
                print('.',end='')
        print()
    print()

# 速い書き方：
# pat = "#." * 310
# while True:
#     h, w = map(int, input().split())
#     if h == w == 0:
#         break

#     for i in range(h):
#         print(pat[i:i + w])
#     print()