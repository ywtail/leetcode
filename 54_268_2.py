# coding:utf-8
# 268. Missing Number 丢失数字
# 69ms beats 39.38%

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for i in range(n):
            ans = ans ^ i ^ nums[i]
        return ans ^ n


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
利用异或。a^b^b=a
假设 nums=[1,5,0,2,4]，
那么 len(nums)=5，说明数的范围是 0~5，索引为 0,1,2,3,4，
利用 nums 和索引异或，相等的值异或结果为 0，在这里结果 ans = 3^5 （索引只到4）
最后 ans^n=3^5^5=3 就是缺失的数字
'''