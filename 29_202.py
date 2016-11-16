# coding:utf-8
# Happy Number

n=int(raw_input())
def isHappy(n):
	"""
	:type n: int
	:rtype: bool
	"""
	if n<=0:
		return False
	else:
		t=[]
		while n!=1:
			n=str(n)
			l=len(n)
			s=0
			for i in range(l):
				s+=int(n[i])**2
			if s==1:
				return True
			if s in t:
				return False
			else:
				t.append(s)
				n=s
		return True

print isHappy(n)

"""
19

True

题目：
编写算法以确定数字是否为“happy”。
快乐号码是由以下过程定义的数字：从任何正整数开始，将数字替换为其数字的平方和，并重复该过程，直到数字等于1（它将保持），否则循环 不断地在一个不包括1的周期中。这个过程以1结束的数字是快乐的数字。
示例：19是一个愉快的数字
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

分析：
没有找到规律，所以直接计算。
"""