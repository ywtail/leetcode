# coding:utf-8
# Excel Sheet Column Number 求字符对应数字

s=raw_input()

def titleToNumber(s):
	"""
	:type s: str
	:rtype: int
	"""
	n=len(s)
	ans=0
	for i in range(1,n+1):
		temp=ord(s[n-i])-ord('A')+1
		ans+=26**(i-1)*temp
	return ans

print titleToNumber(s)

"""
题目：
如果列表标题出现在Excel工作表中，则返回其相应的列号。
例如：
     A→1
     B→2
     C→3
     ... ...
     Z→26
     AA→27
     AB→28

分析：
相当于根据26进制数求10进制数
"""