# coding:utf-8
# Valid Palindrome 有效回文

s=raw_input()

def isPalindrome(s):
	"""
	:type s: str
	:rtype: bool
	"""
	new_s=filter(str.isalnum,s)
	if len(new_s)<2:
		return True
	else:
		head=0
		tail=len(new_s)-1
		while head<tail:
			if new_s[head].lower()==new_s[tail].lower():
				head+=1
				tail-=1
			else:
				return False
		return True

print isPalindrome(s)

"""
题目：
给定一个字符串，确定它是否是一个回文，只考虑字母数字字符，忽略的情况。
例如，
"A man, a plan, a canal: Panama"是一个回文。
"race a car"不是回文。
注意：
你认为字符串可能是空的吗？ 在面试中这是一个很好的问题。
为了这个问题的目的，我们定义空字符串作为有效的回文。

注意：
字符串由数字和字母组成。
在leetcode第11行报错：TypeError: descriptor 'isalnum' requires a 'str' object but received a 'unicode'
编码问题，接收到的是unicode，把Unicode转成str
即将s改为s.encode("utf8")或str(s)
"""