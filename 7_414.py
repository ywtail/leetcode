# coding:utf-8
# Third Maximum Number 第三大的数

nums=map(int,raw_input().split())

def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    newnums=sorted(set(nums))
    if len(newnums)<3:
        return newnums[-1]
    else:
        return newnums[-3]

print thirdMax(nums)

"""
3 3 3 1

3

题目：
给定一个非空的整数数组，返回此数组中的第三个最大数。 
如果不存在，返回最大数。 时间复杂度必须在O（n）中。
Input: [2, 2, 3, 1]
Output: 1

分析：
去除nums列表中重复元素然后排序
"""