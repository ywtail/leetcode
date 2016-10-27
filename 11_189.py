# coding:utf-8
# Rotate Array 旋转数组

nums=map(int,raw_input().split())
k=int(raw_input())

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n=len(nums)
    for i in range(k):
        temp=nums[-1]
        del nums[-1]
        nums.insert(0,temp)

rotate(nums, k)
print nums

"""
1 2 3 4 5 6 7
3

[5, 6, 7, 1, 2, 3, 4]

题目：
将n个元素的数组向右旋转k个步长。
例如，在n = 7和k = 3的情况下，将数组[1,2,3,4,5,6,7]旋转到[5,6,7,1,2,3,4]。
"""