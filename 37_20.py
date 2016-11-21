# coding:utf-8
# Valid Parentheses 括号匹配

s=raw_input()

def isValid(s):
	"""
	:type s: str
	:rtype: bool
	"""
	re={'(':')','[':']','{':'}'}
	stack=[]
	n=len(s)
	for i in range(n):
		if len(stack)==0:
			stack.append(s[i])
		elif stack[-1] in re and re[stack[-1]]==s[i]:
			del stack[-1]
		else:
			stack.append(s[i])
	if len(stack)==0:
		return True
	else:
		return False

print isValid(s)

"""
题目：
给定一个只包含字符'（'，'）'，'{'，'}'，'['和']'的字符串，确定输入字符串是否有效。
括号必须以正确的顺序关闭，“（）”和“（）[] {}”都有效，但“（]”和“（[]]”不是。
"""