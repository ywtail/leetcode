# coding:utf-8
# 136. Single Number 单独的数
# 56ms beats 44.43%

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for x in nums:
            ans ^= x
        return ans


solution = Solution()
print solution.singleNumber([1])
# 1
print solution.singleNumber([1, 2, 3, 1, 4, 3, 2])
# 4

'''
题目：
给定整数数组，除了一个元素之外，每个元素都会出现两次。 找到那个单一的。
注意：
您的算法应具有线性运行时复杂度。 你可以实现它而不使用额外的内存吗？

分析：
异或。出现两次的数 A^A=0
将所有数异或，最后结果就是单独的那个数。
'''