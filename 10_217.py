# coding:utf-8
# Contains Duplicate 包含重复

nums=map(int,raw_input().split())

def containsDuplicate_1(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums)-len(set(nums))>0:
        return True
    else:
        return False

def containsDuplicate_2(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    dic={}
    n=len(nums)
    for i in range(n):
        if nums[i] in dic:
            return True
        else:
            dic[nums[i]]=0
    return False

print containsDuplicate_1(nums)
print containsDuplicate_2(nums)

"""
0 2 1 0 2 0 2

True
True

题目：
给定一个整数数组，找到该数组是否包含任何重复。 如果任何值在数组中至少出现两次，
则函数应返回true，如果每个元素都不同，则函数应返回false。
"""