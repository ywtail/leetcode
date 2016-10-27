# coding:utf-8
# Longest Common Prefix 最长公共前缀

strs=raw_input().split()

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    n=len(strs)
    num=0
    if n>0:
        num=len(strs[0])
        for i in range(1,n):
            if num==0:
                break
            temp=0
            for j in range(num):
                if len(strs[i])<j+1:
                    break
                elif strs[0][j]==strs[i][j]:
                    temp+=1
                else:
                    break
            if temp<num:
                num=temp
    
    s=""
    for i in range(num):
        s+=strs[0][i]
    return s

print longestCommonPrefix(strs)

"""
abcd abc ac

a

题目：
编写一个函数来查找字符串数组中最长的公共前缀字符串。

分析：
贪心：用num记录当前最长公共前缀长度，遍历strs列表中字符串，
对每个字符串最多遍历到num个字符进行匹配
更新num
"""