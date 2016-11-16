# coding:utf-8
# Repeated Substring Pattern 重复的子串模式

st=raw_input()

def repeatedSubstringPattern(st):
        """
        :type str: str
        :rtype: bool
        """
        n=len(st)
        for i in range(1,n):
        	if st[i]==st[0]:
        		temp=st[:i]
        		if n%i==0 and st.count(temp)==n/i:
        			return True
        return False

print repeatedSubstringPattern(st)

"""
a

False

题目：
给定非空字符串检查，如果它可以通过取其子串并将子串的多个副本附加在一起来构造。 
您可以假定给定的字符串仅由小写英文字母组成，其长度不超过10000。
实例1：
输入：“abab”
输出：True
说明：这是子字符串“ab”两次。
实例2：
输入：“aba”
输出：False
实例3：
输入：“abcabcabcabc”
输出：True
说明：这是子字符串“abc”四次。 （和子串“abcabc”两次）。
"""