# coding:utf-8
# Number of Segments in a String 字符串中的段数

s=raw_input()

def countSegments(s):
	"""
	:type s: str
	:rtype: int
	"""
	return len(s.split())
	
print countSegments(s)

"""
题目：
计算字符串中段的数量，其中段被定义为非空格字符的连续序列。
请注意，字符串不包含任何不可打印的字符。
例：
输入："Hello, my name is John"
输出：5
"""