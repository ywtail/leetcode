# coding:utf-8
# Length of Last WordLength of Last Word 最后一个词的长度

s=raw_input()

def lengthOfLastWord(s):
	"""
	:type s: str
	:rtype: int
	"""
	t=s.split()
	if len(t)==0:
		return 0
	else:
		return len(t[-1])

print lengthOfLastWord(s)

"""
题目：
给定一个字符串s由大写/小写字母和空格字符''组成，返回字符串中最后一个字的长度。
如果最后一个字不存在，返回0。
注意：单词定义为仅由非空格字符组成的字符序列。
例如，
给出s =“Hello World”，
返回5。

注意：仅当s仅由空格组成时返回0，‘a  ’返回1
"""