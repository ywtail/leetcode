# coding:utf-8
# 350. Intersection of Two Arrays II 两个数组的交集II
from collections import Counter

nums1=map(int,raw_input().split())
nums2=map(int,raw_input().split())

def intersect(nums1, nums2):
	"""
	:type nums1: List[int]
	:type nums2: List[int]
	:rtype: List[int]
	"""
	dict1=dict(Counter(nums1))
	dict2=dict(Counter(nums2))
	ans=[]
	for k in dict1:
		if k in dict2:
			ans+=[k for i in range(min(dict1[k],dict2[k]))]
	return ans

print intersect(nums1, nums2)

"""
题目：
给定两个数组，写一个函数来计算它们的交集。
例：
给定nums1 = [1,2,2,1]，nums2 = [2,2]，return [2,2]。
注意：
结果中的每个元素应显示为在两个数组中显示的次数。
结果可以是任何顺序。
跟进：
如果给定的数组已经排序怎么办？ 如何优化您的算法？
如果nums1的大小与nums2的大小相比是什么？ 哪种算法更好？
如果nums2的元素存储在磁盘上，并且内存是有限的，这样你不能一次将所有元素加载到内存中呢？

分析：
使用list(set(nums1)&set(nums2))每个元素只显示一次，所以使用Counter来计算。
"""