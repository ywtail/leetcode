# coding:utf-8
# Ransom Note

ransomNote=raw_input()
magazine=raw_input()

def canConstruct(ransomNote, magazine):
	"""
	:type ransomNote: str
	:type magazine: str
	:rtype: bool
	"""
	ran_len=len(ransomNote)
	mag_len=len(magazine)
	if ran_len==0:
		return True
	elif mag_len<ran_len:
		return False
	else:
		remember=[]
		for c in ransomNote:
			if c in remember:
				continue
			else:
				remember.append(c)
				if ransomNote.count(c)>magazine.count(c):
					return False
		return True

print canConstruct(ransomNote, magazine)

"""
abc
cba

True

题目：
给定一个任意的ransomNote字符串和包含所有magazine的字母的另一个字符串，编写一个函数，
如果可以从magazine构建ransomNote，则该函数将返回true; 否则，它将返回false。
magazine字符串中的每个字母只能在您的ransomNote中使用一次。
注意：
您可以假设两个字符串只包含小写字母。
canConstruct（“a”，“b”） - > false
canConstruct（“aa”，“ab”） - > false
canConstruct（“aa”，“aab”） - > true

分析：
题目理解错误。题意只需要某个字母，magazine中出现的次数不少于ransomNote中的就返回True
"""