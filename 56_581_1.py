# coding:utf-8
# 581. Shortest Unsorted Continuous Subarray 最短未排序的连续子数组
# 125ms beats 36.67%

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        left_index = -1 # 待排序数组的左侧索引
        min_num = nums[n - 1]
        for i in range(n - 1)[::-1]:
            if nums[i] > min_num:
                left_index = i
            else:
                min_num = nums[i]
                
        if left_index == -1:
            return 0

        right_index = -1 # 待排序数组的右侧索引
        max_num = nums[0]
        for i in range(1, n):
            if nums[i] < max_num:
                right_index = i
            else:
                max_num = nums[i]

        return right_index - left_index + 1


solution = Solution()
print solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
# 5
print solution.findUnsortedSubarray([1, 3, 5, 8, 4, 2, 1, 9, 7, 10])
# 8

'''
题目：
给定一个整数数组，你需要找到一个连续的子数组，如果你只按升序对这个子数组进行排序，那么整个数组也按升序排序。
您需要找到最短的子阵列并输出其长度。
示例1：
输入：[2，6，4，8，10，9，15]
输出：5
说明：您需要按升序对[6,4,8,10,9]进行排序，使整个数组以升序排列。
注意：
然后输入数组的长度在[1，10,000]的范围内。
输入数组可能包含重复项，因此这里升序表示<=。

分析：
时间复杂度 O(N)，空间复杂度 O(1)
- 先找出待排序数组的左侧索引：
  从右往左遍历，如果当前 num[i]>min_num，则更新左侧索引 left_index=i
- 再找出待排序数组的右侧索引
  从左往右遍历，如果当前 num[i]<max_num，则更新右侧索引 right_index=i
'''