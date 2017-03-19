# coding=utf-8
# 53. Maximum Subarray 最大子数组
# 59ms beats 53.69%

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = nums[0]
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i - 1] < 0:
                dp[i - 1] = 0
            dp[i] = nums[i] + dp[i - 1]
            ans = max(ans, dp[i])
        return ans

nums = map(int, raw_input().split())
solution = Solution()
print solution.maxSubArray(nums)

'''
在数组中找到具有最大和的连续子数组（至少包含一个数字）。
例如，给定数组[-2,1，-3,4，-1,1,1，-5,4]
连续子阵列[4，-1,2,1]具有最大的sum = 6。

使用动态规划做。
'''