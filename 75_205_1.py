# coding:utf-8
# 205. Isomorphic Strings 同构字符串
# 56ms beats 85.31%

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        re = {}
        for i in range(len(s)):  # t中没有两个字符可能映射到相同的字符
            if s[i] not in re:
                re[s[i]] = t[i]
            elif re[s[i]] != t[i]:
                return False
        re = {}
        for i in range(len(s)):  # s中没有两个字符可能映射到相同的字符
            if t[i] not in re:
                re[t[i]] = s[i]
            elif re[t[i]] != s[i]:
                return False
        return True


solution = Solution()
print solution.isIsomorphic('foo', 'bar')
# False
print solution.isIsomorphic('foo', 'baa')
# True
print solution.isIsomorphic('ab', 'aa')
# False
print solution.isIsomorphic('ab', 'ca')
# True

'''
题目：
给定两个字符串s和t，确定它们是否是同构的。
如果s中的字符可以被替换得到t，则两个字符串是同构的。
字符的所有出现必须用另一个字符代替，同时保留字符的顺序。 没有两个字符可能映射到相同的字符，但是一个字符可能映射到自己。
例如，
给定“egg”，“add”，返回true。
给定“foo”，“bar”，返回false。
给予"paper"，"title"，返回true。
注意：
你可以假定s和t都有相同的长度。

分析：
容易理解错题意出错的题。
'ab','ca'返回true，a--c并不表示c--a，b--a也是正确的，但a--b不正确
题中的限制是"没有两个字符可能映射到相同的字符"，
所以字符串s中没有两个字符可能映射到相同的字符，意味着t中某一个字符只能映射到一个字符，而不是两个
而字符串t中没有两个字符可能映射到相同的字符，意味着s中某一个字符只能映射到一个字符，而不是两个
做两遍循环。
'''