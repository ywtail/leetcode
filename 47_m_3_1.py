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
		flag=0
		length=0
		lengths=[]
		n=len(s)
		if n<2:
			return n
		for i in range(n):
			if s[i] not in letter_dic:
				letter_dic[s[i]]=i
				length+=1
			else:
				if flag==0:
					lengths.append(length)
					flag=letter_dic[s[i]]+1
					length-=letter_dic[s[i]]
					letter_dic[s[i]]=i
				else:
					if letter_dic[s[i]]<flag:
						letter_dic[s[i]]=i
						length+=1
					else:
						lengths.append(length)
						length=length-letter_dic[s[i]]+flag
						flag=letter_dic[s[i]]+1
						letter_dic[s[i]]=i
		lengths.append(length)
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

使用letter_dic保存遍历过的字符的最新索引，
使用flag表明字符串的开始位置，
遍历字符串，当遇到重复字符时更新length
"""