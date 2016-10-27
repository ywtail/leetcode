# coding:utf-8
# Best Time to Buy and Sell Stock 最佳买入和卖出股票

prices=map(int,raw_input().split())

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n=len(prices)
    ma=0
    if n>0:
        mi=prices[0]
        for i in range(1,n):
            if prices[i]<mi:
                mi=prices[i]
            if prices[i]-mi>ma:
                ma=prices[i]-mi
    return ma

print maxProfit(prices)

"""
7 1 5 3 6 4

5

题目：
假设你有一个数组，其中第i个元素是第i天给定股票的价格。
如果你只被允许完成最多一个交易，设计一个算法来找到最大利润。
Input: [7, 1, 5, 3, 6, 4]
Output: 5
Input: [7, 6, 4, 3, 1]
Output: 0

分析：
每次只能持有一只股票，所以应该低价买入，高价卖出获得最大利益。
用mi标记最低价，在mi后面的序列中找最高价。
"""