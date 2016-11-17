# coding:utf-8
# Reverse Vowels of a String 反转字符串元音字母

s=raw_input()

def reverseVowels(s):
	"""
	:type s: str
	:rtype: str
	"""
	vowels=['a','e','i','o','u','A','E','I','O','U']
	l=list(s)
	p=0
	q=len(s)-1
	while p<q:
		if l[p] not in vowels:
			p+=1
		if l[q] not in vowels:
			q-=1
		if l[p] in vowels and l[q] in vowels:
			l[p],l[q]=l[q],l[p]
			p+=1
			q-=1
	return ''.join(l)	

print reverseVowels(s)

"""
aA

Aa

题目：
编写一个函数，它接受一个字符串作为输入，只反转一个字符串的元音。
实例1：
给定s =“hello”，返回“holle”。
实例2：
给定s =“leetcode”，返回“leotcede”。
注意：
元音不包括字母“y”。

分析：
字符串中的字符不能直接交换(a,b=b,a)，首先list(s)，再交换，最后join
注意：有可能有大写字母
"""