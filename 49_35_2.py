# coding=utf-8
# 35. Search Insert Position 找插入位置
# 38ms beats 96.90%

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return start


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

使用二分查找，比之前快多了。 
"""
