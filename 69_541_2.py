# coding:utf-8
# 541. Reverse String II 翻转字符串II
# 72ms beats 13.20%


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = s[i:i + k][::-1]
        return ''.join(s)


solution = Solution()
print solution.reverseStr('abcdefg', 2)
# bacdfeg
print solution.reverseStr('abcdefg', 3)
# cbadefg
print solution.reverseStr('abcdefg', 4)
# dcbaefg

'''
题目：
给定一个字符串和一个整数k，您需要从字符串的开头开始计算每2k个字符的第一个k个字符。
如果剩下的字符少于k个字符，则反转所有字符。
如果小于2k但大于或等于k个字符，则反转前k个字符并将另一个作为原始字符。
例：
输入：s =“abcdefg”，k = 2
输出：“bacdfeg”
限制：
1. 该字符串仅由较低的英文字母组成。
2. 给定字符串的长度和k将在范围[1，10000]

分析：
list(s)，步长=2k
'''