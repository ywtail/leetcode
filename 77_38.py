# coding:utf-8
# 38. Count and Say 数和说
# 45ms beats 73.98%

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        re = '1'
        for j in range(n - 1):
            ans = ''
            t = re[0]
            count = 1
            for i in range(1, len(re)):
                if re[i] == re[i - 1]:
                    count += 1
                else:
                    ans += str(count) + t
                    t = re[i]
                    count = 1
            ans += str(count) + t
            re = ans
        return ans


solution = Solution()
print solution.countAndSay(1)
# 1
print solution.countAndSay(8)
# 1113213211

'''
题目：
count-and-say序列前五个如下：
1. 1
2. 11
3. 21
4. 1211
5. 111221
1被读取为“1个1”或11。
11被读取为“2个1”或21。
21被读取为“1个2，然后1个1”或1211。
给定一个整数n，生成count-and-say序列的第n个项。
注意：整数序列中的每个项将被表示为一个字符串。
示例1：
输入：1
输出：“1”
示例2：
输入：4
输出：“1211”

分析：
输入n时，数第n-1个序列中有多少个某数，将"多少个"和"数"存为字符串形式返回。
'''