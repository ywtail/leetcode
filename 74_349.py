# coding:utf-8
# 349. Intersection of Two Arrays 两数组交集
# 39ms beats 96.96%

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))


solution = Solution()
print solution.intersection([1, 2, 2, 1], [2, 2])
# [2]

'''
题目：
给定两个数组，写一个函数来计算它们的交集。
例：
给定nums1 = [1，2，2，1]，nums2 = [2，2]，return [2]。
注意：
结果中的每个元素都必须是唯一的。
结果可以是任何顺序。

分析：
将列表转为集合 set，求交集 &，转为 list返回。
'''