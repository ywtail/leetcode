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
        buy = prices[0]
        profit = 0
        for i in range(1, n):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = max(profit, prices[i] - buy)
        return profit


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
时间复杂度 O(n)，buy 记录当前最小值，profit 记录当前最大利润。
利润计算方法是 prices[i]-buy
'''