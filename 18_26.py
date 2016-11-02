# coding:utf-8
# Remove Duplicates from Sorted Array 从排序的数组中删除重复项

nums=map(int,raw_input().split())

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n=len(nums)
    if n<=1:
        return n
    else:
        p=1
        for i in range(1,n):
            if nums[p]==nums[p-1]:
                del nums[p]
            else:
                p+=1
        return p

print removeDuplicates(nums)

"""
1 1 2 3 2

3

题目：
给定一个排序数组，删除重复的位置，使每个元素只出现一次并返回新的长度。
不要为另一个数组分配额外的空间，必须使用常量内存来做到这一点。
例如，
给定输入数组nums = [1,1,2]
您的函数应返回length = 2，num的前两个元素分别为1和2。超出了新的长度也没关系。

分析：
不能直接返回len(set(nums))，因为测试时要对比nums，而不只是len
"""