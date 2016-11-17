# coding:utf-8
# Reverse String 字符串反转

s=raw_input()

def reverseString(s):
	"""
	:type s: str
	:rtype: str
	"""
	return s[::-1]

print reverseString(s)

"""
题目：
编写一个以字符串作为输入并返回反转字符串的函数。
例：
给定s =“hello”，返回“olleh”。
"""