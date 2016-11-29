# coding:utf-8
# Factorial Trailing Zeroes 阶乘后尾随的零

n=int(raw_input())

def trailingZeroes(n):
	"""
	:type n: int
	:rtype: int
	"""
	ans=0
	while n>4:
		ans+=n/5
		n/=5
	return ans

print trailingZeroes(n)

"""
100

24

题目：
给定一个整数，并返回n!中的尾随零的数目。
注意：您的解决方案应该在对数时间复杂度。

分析：
乘法中的0都是由5（和2）形成的，因此能被多少个5整除就有多少个0。
注意25,625
"""