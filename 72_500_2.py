# coding:utf-8
# 500. Keyboard Row 键盘行
# 35ms beats 92.46%

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1 = set('qwertyuiop')
        line2 = set('asdfghjkl')
        line3 = set('zxcvbnm')
        ans = []
        for word in words:
            w = set(word.lower())
            if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
                ans.append(word)
        return ans


solution = Solution()
print solution.findWords(["Hello", "Alaska", "Dad", "Peace"])
# ['Alaska', 'Dad']

'''
题目：
给出一个单词列表，返回可以使用字母字母输入的单词，仅在美国键盘的一行，如下图所示。
示例1：
输入： ["Hello", "Alaska", "Dad", "Peace"]
输出： ["Alaska", "Dad"]
注意：
您可以多次使用键盘中的一个字符。
您可以假设输入字符串只包含字母。

分析：
参考：https://leetcode.com/problems/keyboard-row/#/solutions
使用 set，先将每一行设置为 set，然后使用 issubset 来检验。
'''