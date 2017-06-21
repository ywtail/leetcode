# coding:utf-8
# 367. Valid Perfect Square 有效的完美平方
# 49ms beats 32.10%

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 1
        right = num
        while left <= right:
            mid = (left + right) / 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False


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
二分法，时间复杂度 O(logn)
使用二分法找 sqrt(n)，每次搜索范围减小一半。
'''