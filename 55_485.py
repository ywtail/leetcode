# coding:utf-8
# 485. Max Consecutive Ones 最大连续1
# 86ms beats 81.21%

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        t = 0
        ans = 0
        for i in range(n):
            if nums[i] == 1:
                t += 1
            else:
                ans = max(ans, t)
                t = 0
        return max(ans,t)


solution = Solution()
print solution.findMaxConsecutiveOnes([1,1,0,1,1,1])
# 3
print solution.findMaxConsecutiveOnes([1,0,1,1,0,1])
# 2

'''
给定二进制数组，找到此数组中连续1的最大数。
示例1：
输入：[1,1,0,1,1,1]
输出：3
说明：前两位数字或最后三位数字是连续1位。
     连续1的最大数量为3。
注意：
输入数组只包含0和1。
输入数组的长度为正整数，不超过10,000
'''