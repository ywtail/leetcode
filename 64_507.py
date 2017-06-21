# coding:utf-8
# 507. Perfect Number 完美数
# 42ms beats 95.30%
import math


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 or num % 2 == 1:
            return False
        sum_all = 1
        n = int(math.sqrt(num))
        for i in range(2, n + 1):
            if num % i == 0:
                sum_all += i + num / i
        return sum_all == num


solution = Solution()
print solution.checkPerfectNumber(16)
# False
print solution.checkPerfectNumber(28)
# True
print solution.checkPerfectNumber(20996011)
# False

'''
题目：
我们定义Perfect Number是一个正整数，等于除了它本身的所有正除数之和。
现在，给定一个整数n，写一个函数，当它是一个完美数字时返回true，否则返回false。
例：
输入：28
输出：真
说明：28 = 1 + 2 + 4 + 7 + 14
注意：输入号n不会超过100,000,000。（1E8）

分析：
易错：输入有可能是负数。完美数是正整数而输入时整数。
注意：
1. 不用考虑 num=i*i 时，i 被加了两遍。因为平方数不可能是完美数：https://zh.wikipedia.org/wiki/%E5%AE%8C%E5%85%A8%E6%95%B0
2. 还可以查到，目前没有发现奇完美数。题中指出 num 的范围不会超过 100,000,000，在这个范围内，完美数都是偶数。
'''