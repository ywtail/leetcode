# coding:utf-8
# 389. Find the Difference 找不同
# 42ms beats 93.97%

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        x = list(s) + list(t)
        ans = 0
        for i in range(len(x)):
            ans ^= ord(x[i])
        return chr(ans)


solution = Solution()
print solution.findTheDifference('abcd', 'abcde')
# e
print solution.findTheDifference('abcd', 'abecd')
# e

'''
题目：
给定两个字符串s和t，它们只包含小写字母。
字符串t由随机混合字符串s生成，然后在随机位置添加一个字母。
找到在t中添加的字母。
例：
输入：
s =“abcd”
t =“abcde”
输出：
e
说明：
'e'是添加的字母。

分析：
将字符转为数字，使用异或
'''