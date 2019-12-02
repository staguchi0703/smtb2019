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
import itertools as it

num = int(input())

item_number = num//100

if item_number>= 20:
    item_number = 20

res_list = []
candi_list = list(it.combinations_with_replacement([100, 101, 102, 103, 104, 105], item_number))
candi_ans_list = [sum(item) for item in candi_list]

if num >= 2000:
    print(1)
else:

    if num in candi_ans_list:
        print(1)
    else:
        print(0)




