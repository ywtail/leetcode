# coding:utf-8
# Contains Duplicate II 包含重复II

nums=map(int,raw_input().split())
k=int(raw_input())

def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    n=len(nums)
    dic={}
    for i in range(n):
        if nums[i] in dic:
            if i-dic[nums[i]][-1]<=k:
                return True
            else:
                dic[nums[i]].append(i)
        else:
            dic[nums[i]]=[i]
    return False

print containsNearbyDuplicate(nums, k)

"""
0 2 1 0 2 0 2
2

True

题目：
给定整数和整数k的数组，找出在阵列中是否存在两个不同的索引i和j，
使得nums [i] = nums [j]并且i和j之间的差最大为k。

分析：
用dic存当前值和索引列表 {nums[i]:[index1,index2]}，
如果有相同的值出现，检查与索引列表中最后一个值是否相差不大于k，
如果不满足则将索引存入dic的索引列表部分。
"""