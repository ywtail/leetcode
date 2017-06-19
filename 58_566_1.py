# coding:utf-8
# 566. Reshape the Matrix 重塑矩阵
# 252ms beats 11.84%

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        n = len(nums[0]) * len(nums)
        ans = []
        if n == r * c:
            t = 0
            temp = []
            for x in nums:
                for y in x:
                    temp.append(y)
                    t += 1
                    if t % c == 0:
                        ans.append(temp)
                        temp = []
            return ans
        else:
            return nums


solution = Solution()
print solution.matrixReshape([[1, 2], [3, 4]], 1, 4)
# [[1, 2, 3, 4]]
print solution.matrixReshape([[1, 2], [3, 4]], 2, 4)
# [[1, 2], [3, 4]]
print solution.matrixReshape([[1, 2], [3, 4]], 4, 1)
# [[1], [2], [3], [4]]

'''
题目：
在MATLAB中，有一个非常有用的函数叫做“reshape”，它可以将矩阵重新形成一个不同大小的矩阵，但是保持其原始数据。
给出一个由二维数组表示的矩阵，两个正整数r和c分别表示所需重组矩阵的行号和列号。
重新组合的矩阵需要以与它们相同的行遍历顺序填充原始矩阵的所有元素。
如果具有给定参数的“reshape”操作是可行且合法的，则输出新的重构矩阵;否则，输出原始矩阵。
示例1：
输入：
nums =
[[1,2]，
 [3,4]
r = 1，c = 4
输出：
[[1,2,3,4]]
说明：
数字的行遍历是[1,2,3,4]。新的重构矩阵是一个1 * 4矩阵，使用上一个列表逐行填充。
示例2：
输入：
nums =
[[1,2]，
 [3,4]
r = 2，c = 4
输出：
[[1,2]，
 [3,4]
说明：
无法将2 * 2矩阵重塑为2 * 4矩阵。所以输出原来的矩阵。
注意：
给定矩阵的高度和宽度在[1,100]范围内。
给定的r和c都是正的。

分析：
求得矩阵中元素总个数为 n，
如果 n!=r*c，则直接返回原矩阵；
否则，遍历 nums 中的每个元素，并计数，当当前计数是 c 的整数倍时，ans.append(temp)
'''