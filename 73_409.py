# coding:utf-8
# 409. Longest Palindrome 最长回文长度
# 49ms beats 71.69%

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        re = {}
        n = len(s)
        for i in range(n):
            if s[i] not in re:
                re[s[i]] = 1
            else:
                re[s[i]] += 1
        ans = 0
        for x in re:
            ans += re[x] / 2 * 2
        if ans < n:
            return ans + 1
        return ans


solution = Solution()
print solution.longestPalindrome('abccccdd')
# 7

'''
题目：
给定一个由小写或大写字母组成的字符串，找到可以用这些字母构建的最长的回文长度。
这是区分大小写的，例如“Aa”在这里不被视为回文。
注意：
假定给定字符串的长度不会超过1,010。
例：
输入：
“abccccdd”
输出方式：
7
说明：
可以建造的最长的回文是“dccaccd”，长度为7。

分析：
回文串除了正中心的字符出现奇数次，其他字符都出现偶数次。
先统计所有字符在输入中出现的次数，再求 re[x] / 2 * 2 的和。

另外的一种方法是，在统计出现次数时，第一次出现加入字典，第二次从字典删除，同时 count++，
最后求得的count是输入中一共有多少个偶数对，返回 count*2 或 count*2+1
'''