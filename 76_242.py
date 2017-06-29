# coding:utf-8
# 242. Valid Anagram 有效变形词
# 78ms beats 79.36%

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        re_s = [0] * 26
        for x in s:
            re_s[ord(x) - ord('a')] += 1
        for y in t:
            re_s[ord(y) - ord('a')] -= 1
            if re_s[ord(y) - ord('a')] < 0:  # 不需要再遍历是否都=0
                return False
        return True


solution = Solution()
print solution.isAnagram('anagram', 'nagaram')
# True
print solution.isAnagram('rat', 'car')
# False

'''
题目：
给定两个字符串s和t，写一个函数来确定t是否是s的变形词。
例如，
s =“anagram”，t =“nagaram”，返回true。
s =“rat”，t =“car”，返回false。
注意：
您可以假定字符串只包含小写字母。

分析：
如果长度不同返回false。
遍历s用列表记录字符出现的次数，
遍历t，在t中出现的就在re_s中-1，如果有负值，就返回false。
'''