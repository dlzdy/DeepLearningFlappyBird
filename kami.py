# -*- coding=utf8 -*-
#cards = (1, 2, 3, 5, 6, 8, 10, 20, 50, 100)
cards = (100, 50, 20, 10, 8, 6, 5, 3, 2, 1)
result = []

# 目标
target = 88
target = 256
# 循环
left = target
while left > 0:
    for card in cards:
        temp_count = left // card
        if temp_count > 0 :
            print('%d = %d'% (card,temp_count))
            left = left - temp_count * card # 剩下的钱
        if left == 0:
            break


