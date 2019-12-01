# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\C\C_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
line = input()

if int(line) >= 100:
    num = int(line[-2:])
    item_number = int(line[:-2])



    res_list = []
    a = 5
    while True:
        if num == 0:
            break
        for _ in range(num//a):
            res_list.append(a)

        num = num % a

        if 1<= num <= 4:
            res_list.append(num)
            break


    # print(res_list)

    if len(res_list) > item_number:
        print(0)
    else:
        print(1)

else:
    print(0)




