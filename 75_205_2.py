# coding:utf-8
# 205. Isomorphic Strings 同构字符串
# 69ms beats 54.34%

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        re_s = [0] * 256
        re_t = [0] * 256
        n = len(s)
        for i in range(n):
            if re_s[ord(s[i])] != re_t[ord(t[i])]:
                return False
            re_s[ord(s[i])] = i + 1
            re_t[ord(t[i])] = i + 1
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
s和t不一定只包含字母，所以 re 长度 256。
使用 re_s 和 re_t 记录字符对应的索引
'''