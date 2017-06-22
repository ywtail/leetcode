# coding:utf-8
# 551. Student Attendance Record I 学生出勤记录
# 49ms beats 39.22%


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0  # 记录A数量
        l = 0
        for x in s:
            if x == 'L':
                l += 1
                if l > 2:
                    return False
            else:
                l = 0
                if x == 'A':
                    a += 1
                    if a > 1:
                        return False
        return True


solution = Solution()
print solution.checkRecord('PPALLP')
# True
print solution.checkRecord('PPALLL')
# False
print solution.checkRecord('PPALLPLL')
# True

'''
题目：
您将获得一个代表学生出勤记录的字符串。 该记录仅包含以下三个字符：
'A'：离开
'L'：迟到
'P'：在
如果出席记录不包含多于一个“A”（缺席）或超过两个连续的“L”（后期），学生可以获得奖励。
你需要返回学生是否可以根据出勤记录得到奖励。
'''