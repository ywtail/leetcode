# coding:utf-8
# Arranging Coins 排列硬币

import math
n=int(raw_input())

def arrangeCoins(n):
    """
    :type n: int
    :rtype: int
    """
    temp=int(math.sqrt(2*n))
    ans=temp-1 if temp*(temp+1)>2*n else temp
    return ans

print arrangeCoins(n)

"""
11

4

题目：
你总共有n个硬币，你想形成一个楼梯形状，其中每第k行必须有正好k个硬币。
给定n，找到可以形成的完整楼梯行的总数。
n是一个非负整数，并且在32位有符号整数的范围内。
实例1：
n = 5
硬币可以形成以下行：
¤
¤¤
¤¤
因为第三行是不完整的，我们返回2。
实例2：
n = 8
硬币可以形成以下行：
¤
¤¤
¤¤¤
¤¤
因为第4行不完整，我们返回3。
"""