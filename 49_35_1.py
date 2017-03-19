# coding=utf-8
# 35. Search Insert Position
# 45ms beats 60.15%

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if target > nums[-1]:
            return n
        else:
            for i in range(n):
                if target <= nums[i]:
                    return i


nums = map(int, raw_input().split())
target = int(raw_input())

solution = Solution()
print solution.searchInsert(nums, target)

"""
题目：https://leetcode.com/problems/search-insert-position/#/description
给定一个排序数组和一个目标值，如果找到目标，则返回索引。 如果没有，返回索引的位置，如果它是按顺序插入。
您可以假设数组中没有重复项。

这里有几个例子。
[1,3,5,6]，5→2
[1,3,5,6]，2→1
[1,3,5,6]，7→4
[1,3,5,6]，0→0

最简单的遍历，插入。
考虑到如果target在最后，则依然遍历n次，所以加了个判断。
因为题目默认nums不为空，所以在代码中也不考虑nums为空的情况。
"""