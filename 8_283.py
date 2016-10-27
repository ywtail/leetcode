# coding:utf-8
# Move Zeroes 移动零

nums=map(int,raw_input().split())

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n=len(nums)
    q=n-1
    while nums[q]==0 and q>0:
    	q-=1
    if q>0:
    	p=0
    	while p<q:
    		if nums[p]==0: #由于有del操作，所以不用p+=1
    			del nums[p]
    			nums.append(0)
    			q-=1
    		else:
    			p+=1

moveZeroes(nums)
print nums

"""
0 0 1 0 2 0

[1, 2, 0, 0, 0, 0]

题目：
给定一个数组nums，写一个函数将所有的0移动到它的结尾，同时保持非零元素的相对顺序。
例如，给定nums = [0，1，0，3，12]，在调用函数之后，nums应该是[1,3,12,0,0]。
注意：
您必须在原地执行此操作，而不必创建数组的副本。
最小化操作的总数。

分析：
例如输入0 0 1 0 0
q指针从后往前定位第一个非0元素的位置，避免将原本在末尾的0移动到最后的多余操作。
p指针从前往后，遇到0时将其移动到最后
"""