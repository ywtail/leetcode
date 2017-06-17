# coding:utf-8
# 268. Missing Number 丢失数字
# 62ms beats 50.28%

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        bucket = [0] * (n + 1)
        for x in nums:
            bucket[x] = 1
        print bucket
        for i in range(n + 1):
            if bucket[i] == 0:
                return i


solution = Solution()
print solution.missingNumber([0, 1, 3])
# 2
print solution.missingNumber([0])
# 1
print solution.missingNumber([1, 0])
# 2

'''
题目：
给定一个包含从0，1，2，...，n中取出的n个不同数字的数组，找到数组中缺少的数组。
例如，
给定nums = [0，1，3]返回2。
注意：
您的算法应该运行在线性运行时的复杂性。 你可以使用只有恒定的额外的空间复杂性实现它吗？

分析：
容易理解错题意。
利用桶
'''