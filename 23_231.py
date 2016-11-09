# coding:utf-8
# Power of Two 二的幂

n=int(raw_input())

def isPowerOfTwo(n):
	"""
	:type n: int
	:rtype: bool
	"""
	if n<=0:
		return False
	elif n==1:
		return True
	else:
		while n>1:
			if n%2==0:
				n=n/2
			else:
				return False
		return True

print isPowerOfTwo(n)

"""
2

True

题目：
给定一个整数，写一个函数来确定它是否为2的幂。
（注意：有可能是0或负数）
"""