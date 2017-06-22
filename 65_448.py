# coding:utf-8
# 448. Find All Numbers Disappeared in an Array 找出数组中所有未出现的数
# 339ms beats 56.64%


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(nums)
        for i in range(n):
            t = abs(nums[i]) - 1
            if nums[t] > 0:
                nums[t] = -nums[t]
        for i in range(n):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans


solution = Solution()
print solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
# [5, 6]

'''
题目：
给定一个整数数组，其中1≤a[i]≤n（n =数组大小），某些元素出现两次，而其他元素出现一次。
找到不出现在这个数组中的[1，n]包含的所有元素。
你可以在没有额外空间的情况下运行吗？ 您可以假设返回的列表不计入额外的空间。
例：
输入：
[4,3,2,7,8,2,3,1]
输出方式：
[5,6]

分析：
这一题的方法十分巧妙。
遍历 nums，使用 nums[i]-1 作索引，将对应位置的元素取负（nums [nums [i] -1] = -nums [nums [i] -1]）
即只要出现了的元素，对应索引位置的元素一定是负数。
第二次遍历nums，如果对应元素是正数，说明这个索引没有出现过。
索引（+1）即是 Disappeared 的数。

除了索引对应数取负，还可以对应数 +n
第二次遍历如果<n，就是 Disappeared 的数
'''