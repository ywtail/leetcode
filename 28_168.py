# coding:utf-8
# Excel Sheet Column Title 求数字对应字母

n=int(raw_input())

def convertToTitle(n):
	"""
	:type n: int
	:rtype: str
	"""
	ans=""
	while n!=0:
		if n%26==0:
			ans='Z'+ans
			n=(n-26)/26 #这一步易错
		else:
			ans=chr(n%26-1+ord('A'))+ans
			n/=26
	return ans

print convertToTitle(n)

"""
728

AAZ

题目：
给定一个正整数，返回其相应的列标题，如出现在Excel表。
例如：
     1→A
     2→B
     3→C
     ... ...
     26 - > Z
     27→AA
     28→AB

分析：
十进制转26进制，当n%26==0时，n=(n-26)/26 这一步易错
"""