# coding:utf-8
# Two Sum II - Input array is sorted 两数求和II-输入数组有序
# 56ms beats 33.28%

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        re = {}
        for i in range(n):
            if numbers[i] in re:
                return [re[numbers[i]], i + 1]
            t = target - numbers[i]
            if t not in re:
                re[t] = i + 1


solution = Solution()
print solution.twoSum([2, 3, 4], 6)
# [1, 3]
print solution.twoSum([2, 7, 11, 15], 9)
# [1, 2]
print solution.twoSum([0, 0, 0, 2, 7, 8, 9, 10, 11, 15], 26)
# [9, 10]

'''
题目：
给定一个已经按升序排序的整数数组，找到两个数字，使它们相加到一个特定的目标数。
函数twoSum应该返回两个数字的索引，使其相加到目标，其中index1必须小于index2。 请注意，您返回的答案（index1和index2）都不是基于零的。
您可以假设每个输入都将具有一个解决方案，您可能不会使用相同的元素两次。
输入：numbers = {2，7，11，15}，target = 9
输出：index1 = 1，index2 = 2

分析：
使用一个 re 字典存储需要查找的数字和当前 index，
遍历numbers，如果当前数字在 re 中，则返回
'''