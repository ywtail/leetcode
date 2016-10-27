# coding:utf-8
# Majority Element 多数元素

nums=map(int,raw_input().split())

def majorityElement_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n=len(nums)
    dic={}
    for i in range(n):
        if nums[i] in dic:
            dic[nums[i]]+=1
        else:
            dic[nums[i]]=1
        if dic[nums[i]]>n/2:
                return nums[i]

def majorityElement_2(snums):
    """
    :type nums: List[int]
    :rtype: int
    """
    from collections import Counter
    n=len(nums)
    num=dict(Counter(nums))
    for key in num:
        if num[key]>n/2:
            return key

print majorityElement_1(nums)
print majorityElement_2(nums)

"""
2 9 2 2 1

2
2

题目：
给定一个大小为n的数组，找到多数元素。 多数元素是出现超过n / 2倍的元素。
您可以假定数组非空，且多数元素始终存在于数组中。
"""