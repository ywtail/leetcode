# coding:utf-8

nums=map(int,raw_input().split())
target=int(raw_input())

def twoSum(nums, target):
	n=len(nums)
	for i in range(n):
	    for j in range(i+1,n):
	        if nums[i]+nums[j]==target:
	            return [i,j]

print twoSum(nums, target)

"""
2 7 11 5
9

[0,1]

题目：
给定一个整数数组，返回两个数字的索引，使得它们相加到一个特定的目标。
您可以假设每个输入都有一个解决方案。
"""