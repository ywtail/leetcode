# coding:utf-8
# Minimum Moves to Equal Array Elements 使数组元素相等的最小移动数

nums=map(int,raw_input().split())

def minMoves(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n=len(nums)
    mi=min(nums)
    ans=0
    for i in range(n):
        ans+=(nums[i]-mi)
    return ans

print minMoves(nums)

"""
1 9 8 7

21

题目：
给定大小为n的非空整数数组，找到使所有数组元素相等所需的最小移动数，其中移动将n-1个元素递增1。
例：
输入：
[1,2,3]
输出：
3
说明：
只需要三个动作（记住每个动作增加两个元素）：
[1,2,3] => [2,3,3] => [3,4,3] => [4,4,4]

分析：
一般思路：
每次除了最大值，其他元素都+1，直到所有元素相等。
规律：
通过观察发现，每一次最小的元素都+1，而最大的元素是轮流的，
如果给数从小到大排序形成数组a，那么第一次a[n-1]最大，当最小元素调整到与a[n-1]相等时，
a[n-2]最大，以此类推。
每次除了最大元素，其他元素都+1，所以差值是不变的，
用原数组的元素轮流减去最小元素的和就是最小移动数。
"""