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
        re = {}  # 记录s中各元素出现个数
        for x in s:
            if x in re:
                re[x] += 1
            else:
                re[x] = 1
        for y in t:
            if y not in re or re[y] == 0:
                return y
            re[y] -= 1


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
使用 re 记录 s 中各元素出现个数
遍历 t，如果某个字母在 re 中不存在或个数减为 0，就是添加的字母。
'''