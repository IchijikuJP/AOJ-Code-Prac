#goto 文は、C/C++言語などで使うことのできる文で、
# 実行されると無条件に指定されたラベルに処理が飛びます。
# 例えば goto CHECK_NUM; という文が実行されると、
# プログラムの中で CHECK_NUM: と書かれた行に処理が移ります。
# この機能を使って、繰り返し処理なども実現することができます
n =int(input())
i  = 1
print('',end=' ')
for i in range(3,n+1) :
    if  i % 3 == 0 :
        print(i, end=' ')
    elif   i % 10 == 3 :
        print(i, end=' ')
    elif ("3" in str(i)) :
        print(i, end=' ')  


