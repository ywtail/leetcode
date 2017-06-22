# coding:utf-8
# 121. Best Time to Buy and Sell Stock 买卖股票
# 59ms beats 34.93%


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        max_cur = 0
        max_sofar = 0
        for i in range(1, n):
            max_cur = max(0, max_cur + prices[i] - prices[i - 1])
            max_sofar = max(max_sofar, max_cur)
        return max_sofar


solution = Solution()
print solution.maxProfit([7, 1, 5, 3, 6, 4])
# 5
print solution.maxProfit([7, 6, 4, 3, 1])
# 0


'''
题目：
说你有一个数组，第i个元素是第i天给定股票的价格。
如果只允许最多完成一个交易（即购买一个交易，并出售股票一个），则设计一个算法来找到最大利润。
示例1：
输入：[7，1，5，3，6，4]
输出：5
最大差= 6-1 = 5（不是7-1 = 6，因为售价需要大于购买价格）
示例2：
输入：[7，6，4，3，1]
输出：0
在这种情况下，没有交易完成，即最大利润= 0。

分析：
Kadane算法：https://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E5%AD%90%E6%95%B0%E5%88%97%E9%97%AE%E9%A2%98
这一题的逻辑与"最大子数列"（找到一个连续的子数列，使该子数列的和最大）相同。
求 [7, 1, 5, 3, 6, 4] 最大利润，相当于求 [0,-6,4,-2,3,-2] 最大子数列。
max_cur的值分别为：0,0,4,2,5,3
Kadane算法扫描一次整个数列的所有数值，在每一个扫描点计算以该点数值为结束点的子数列的最大和（正数和）。
该子数列有可能为空，或者由两部分组成：以前一个位置为结束点的最大子数列、该位置的数值。
'''