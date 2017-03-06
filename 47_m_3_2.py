# coding:utf-8
# 3. Longest Substring Without Repeating Characters不重复字符最长子串
# 105ms

class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		letter_dic={}
		flag=-1
		lengths=[0] #如果字符串为空
		n=len(s)
		for i in range(n):
			if s[i] in letter_dic and letter_dic[s[i]]>=flag: #在开始位置之前出现过，将其改为现在位置即可
				flag=letter_dic[s[i]]
			letter_dic[s[i]]=i
			lengths.append(i-flag)
					
		print lengths
		return max(lengths)

solution=Solution()
s=raw_input()
print solution.lengthOfLongestSubstring(s)

"""
给定一个字符串，找到不重复字符的最长子字符串的长度。
例子：
给定“abcabcbb”，答案是“abc”，长度为3。
给定“bbbbb”，答案是“b”，长度为1。
给定“pwwkew”，答案是“wke”，长度为3.注意答案必须是一个子串，“pwke”是一个子序列，而不是一个子串。

使用letter_dic保存遍历过的字符的索引，
如果有重复出现，则更新flag，使flag表明重复字符的上一个位置，即新字符串开始位置
每一步都append(i-flag)，这样不用考虑哪一步append

注意字符串可能为空，因此lengths初始是[0]
"""