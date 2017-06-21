# coding:utf-8
# 367. Valid Perfect Square 有效的完美平方
# 56ms beats 18.34%

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0


solution = Solution()
print solution.isPerfectSquare(16)
# True
print solution.isPerfectSquare(8)
# False

'''
题目：
给定一个正整数num，写一个函数返回True，如果num是一个完美的平方，否则返回False。
注意：不要使用任何内置的库函数，如sqrt。
示例1：
输入：16
返回值：True
示例2：
输入：14
返回：False

分析：
因为平方数 x = 1 + 3 + 5 + 7 + 9 + 11 + 13 + ...
'''