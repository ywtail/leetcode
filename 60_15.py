# coding:utf-8
# 15. 3Sum
# 1145ms beats 53.46%

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                if nums[left] + nums[right] > -nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    if left == i + 1 or nums[left - 1] != nums[left]: # 注意是 left==i+1
                        ans.append([nums[i], nums[left], nums[right]])
                    left += 1 # 要找到所有匹配的，所以 left++，right--
                    right -= 1
        return ans


solution = Solution()
print solution.threeSum([-1, 0, 1, 2, -1, -4])
# [[-1, -1, 2], [-1, 0, 1]]


'''
题目：
给定n个整数的数组S，S中有元素a，b，c，使得+ b + c = 0？ 查找数组中所有独特的三元组，它们的总和为零。
注意：解决方案集不能包含重复的三元组。
例如，给定数组S = [-1,0,1,2，-1，-4]，
解决方案是：
[
   [-1,0,1]，
   [-1，-1,2]
]

分析：
先对数组排序，然后对每个 num[i]，寻找 num[left]+num[right]==0-num[i] 的二元组。
因为要不重复打印，所以需要注意很多细节。
'''