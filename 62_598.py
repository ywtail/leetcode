# coding:utf-8
# 598. Range Addition II 范围增加II
# 52ms beats 44.94%

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if len(ops) == 0:  # 易漏
            return m * n
        r = ops[0][0]
        c = ops[0][1]
        for a, b in ops:
            r = min(r, a)
            c = min(c, b)
        return r * c


solution = Solution()
print solution.maxCount(3, 3, [[2, 2], [3, 3]])
# 4
print solution.maxCount(3, 7, [])
# 21

'''
题目：
给定一个m * n矩阵M，初始化为全0和几个更新操作。
操作由2D阵列表示，每个操作由具有两个正整数a和b的数组表示，
这意味着对于所有 0 <= i <a 和 0 <= j <b，应该将 M[i][j]加1 。
执行所有操作后，您需要计算并返回矩阵中最大整数的数量。
示例1：
输入：
m = 3，n = 3
operations = [[2,2]，[3,3]]
输出：4
说明：
最初，M =
[[0，0，0]，
  [0，0，0]，
  [0，0，0]]

执行[2,2]后，M =
[[1，1，0]
  [1，1，0]，
  [0，0，0]]

执行[3,3]后，M =
[[2，2，1]
  [2，2，1]
  [1,1,1]]

所以M中的最大整数为2，在M中有四个。因此返回4。
注意：
1. m和n的范围是[1,40000]。
2. a的范围是[1，m]，b的范围是[1，n]。
3. 操作范围不超过10,000。

分析：
注意考虑 ops=[] 的情况。
ops 不为空时，+1 的行数取 a 的最小值，列数取 b 的最小值。
这是因为每次 +1 的范围是 0 <= i <a 和 0 <= j <b，即每次左上角都 +1，所以左上角最大。
'''