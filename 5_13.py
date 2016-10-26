# coding:utf-8
# Roman to Integer

s=raw_input()

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    n=len(s)
    r={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    if n==1:
        return r[s]
    else:
        ans=0
        now=0
        for i in range(1,len(s)):
            if r[s[i]]<r[s[i-1]]:
                ans+=r[s[i-1]]
                now=0
            elif r[s[i]]==r[s[i-1]]:
                ans+=r[s[i-1]]
                now+=r[s[i-1]]
            else:
                ans-=(2*now+r[s[i-1]])
                now=0
        ans+=r[s[n-1]]
        return ans

print romanToInt(s)

"""
IIV

3

题目：
给定罗马数字，将其转换为整数。
输入保证在1到3999的范围内。

分析：
建立罗马字符和整数之间的映射关系字典r
遍历输入字符串，如果前面字符代表的数字比后面字符大，直接累加
否则，用后面大的字符减去前面小的字符
（用now存储，由于now加了一遍，所以需要减两遍），然后将结果累加到ans上
"""