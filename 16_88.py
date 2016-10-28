# coding:utf-8
# Merge Sorted Array 合并排序数组

nums1=map(int,raw_input().split())
m=int(raw_input())
nums2=map(int,raw_input().split())
n=int(raw_input())

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    nums1[m:]=nums2[:n]
    nums1.sort()

merge(nums1, m, nums2, n)
print nums1

"""
题目：
给定两个排序的整数数组nums1和nums2，将nums2合并为nums1作为一个排序的数组。
注意：
您可以假设nums1有足够的空间（大于或等于m + n的大小）来容纳nums2中的其他元素。 
在nums1和nums2中初始化的元素的数量分别为m和n。

分析：
根据测试用例，m不是num1的大小，是需要操作的nums1中元素的个数。
测试用例如下：
[0]
0
[1]
1

[1]
"""