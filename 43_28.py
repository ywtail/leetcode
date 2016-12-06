# coding:utf-8
# Implement strStr()

haystack=raw_input()
needle=raw_input()

def strStr(haystack, needle):
	"""
	:type haystack: str
	:type needle: str
	:rtype: int
	"""
	return haystack.find(needle)

print strStr(haystack, needle)

"""
题目：
实现strStr（）。
返回haystack中needle的第一次出现的索引，如果needle不是haystack的一部分，则返回-1。
"""