# coding:utf-8
# 557. Reverse Words in a String III 翻转字符串中的词III
# 52ms beats 68.17%


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sentence = s.split()
        n = len(sentence)
        for i in range(n):
            sentence[i] = sentence[i][::-1]
        return ' '.join(sentence)


solution = Solution()
print solution.reverseWords('')
#
print solution.reverseWords(' ')
#
print solution.reverseWords("Let's take LeetCode contest")
# s'teL ekat edoCteeL tsetnoc

'''
题目：
给定一个字符串，你需要颠倒一个句子中每个单词中的字符顺序，同时保留空格和初始单词顺序。
示例1：
输入：“Let's take LeetCode contest”
输出：“s'teL ekat edoCteeL tsetnoc”
注意：在字符串中，每个单词都以单个空格分隔，字符串中不会有任何额外的空格。

分析：
将句子切为词，每个词翻转 [::-1]，再 join
'''