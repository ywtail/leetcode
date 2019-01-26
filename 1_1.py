# coding:utf-8
# 1.Two Sum 两数之和

nums=map(int,raw_input().split())
target=int(raw_input())

# 方法一 16.10.26
def twoSum(nums, target):
	n=len(nums)
	for i in range(n):
	    for j in range(i+1,n):
	        if nums[i]+nums[j]==target:
	            return [i,j]

# 方法二 19.1.27
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    m_dict={}
    for i in range(len(nums)):
        if nums[i] in m_dict:
            return [m_dict[nums[i]],i]
        m_dict[target-nums[i]]=i

print twoSum(nums, target)

"""
2 7 11 5
9

[0,1]

题目：
https://leetcode-cn.com/problems/two-sum/
给定一个整数数组，返回两个数字的索引，使得它们相加到一个特定的目标。
您可以假设每个输入都有一个解决方案。
解答：
http://ywtail.github.io/2019/01/26/leetcode-1-%E4%B8%A4%E6%95%B0%E4%B9%8B%E5%92%8C/
"""