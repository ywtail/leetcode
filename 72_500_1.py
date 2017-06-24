# coding:utf-8
# 500. Keyboard Row 键盘行
# 55ms beats 16.79%

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        re = {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1, 'Q': 1, 'W': 1, 'E': 1,
              'R': 1, 'T': 1, 'Y': 1, 'U': 1, 'I': 1, 'O': 1, 'P': 1, 'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2,
              'j': 2, 'k': 2, 'l': 2, 'A': 2, 'S': 2, 'D': 2, 'F': 2, 'G': 2, 'H': 2, 'J': 2, 'K': 2, 'L': 2, 'z': 3,
              'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3, 'Z': 3, 'X': 3, 'C': 3, 'V': 3, 'B': 3, 'N': 3, 'M': 3}
        ans = []
        for word in words:
            flag = 1
            t = re[word[0]]
            for w in word:
                if re[w] != t:
                    flag = 0
                    break
            if flag:
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
将每个字母的行号存在字典中，遍历每个词，如果所有字母都在同一行，就加入ans
'''