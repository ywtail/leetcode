# coding:utf-8
# Power of Three 三的幂

n=int(raw_input())

def isPowerOfThree(n):
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
			if n%3==0:
				n=n/3
			else:
				return False
		return True

print isPowerOfThree(n)

"""
3

True

题目：
给定一个整数，写一个函数来确定它是否为3的幂。
跟进：
你能不使用任何循环/递归？
"""