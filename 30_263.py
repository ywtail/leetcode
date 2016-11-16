# coding:utf-8
# Ugly Number

num=int(raw_input())

def isUgly(num):
	"""
	:type num: int
	:rtype: bool
	"""
	if num==0: #漏掉0会进入死循环
		return False
	else:
		while num!=1:
			if num%2==0:
				num=num/2
			elif num%3==0:
				num=num/3
			elif num%5==0:
				num=num/5
			else:
				return False
		return True

print isUgly(num)

"""
24

True

题目：
编写程序以检查给定的数字是否是一个丑陋的数字。
丑数是正数，其素因子只包括2,3,5。例如，6,8是丑陋的，而14不丑陋，因为它包括另一个素因子7。
注意，1通常被视为丑陋的数字。
"""