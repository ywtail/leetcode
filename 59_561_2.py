# coding:utf-8
# 561. Array Partition I 数组分区I；简化写法；range(0,n,2)设置步长
# 145ms beats 51.29%

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = sorted(nums)
        ans = 0
        for i in range(0,n,2):
            ans += nums[i]
        return ans


solution = Solution()
print solution.arrayPairSum([1, 4, 3, 2])
# 4

'''
题目：
给定一个2n个整数的数组，你的任务是将这些整数分成n对整数，如（a1，b1），（a2，b2），...，（an，bn），这使得（ai， bi）对于所有i从1到n尽可能大。
示例1：
输入：[1,4,3,2]
输出：4
说明：n为2，最大对数为4 = min（1,2）+ min（3,4）。
注意：
n是正整数，在[1，10000]的范围内。
数组中的所有整数将在[-10000，10000]的范围内。

分析：
先排序，然后取偶数索引（相邻两数中较小的数）的数相加，即为结果。
在这里设置步长，for 循环次数减小一半。
'''