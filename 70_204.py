# coding:utf-8
# 204. Count Primes 素数数
# 869ms beats 62.89%

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        re = [1] * n
        for i in range(2, int(n ** 0.5) + 1):  # 只需要到 sqrt(n)
            if re[i]:
                for j in range(i * i, n, i):  # 从i*i开始，不是2*
                    re[j] = 0
        return sum(re) - 2


solution = Solution()
print solution.countPrimes(3)
# 1
print solution.countPrimes(12)
# 5
print solution.countPrimes(100)
# 25
print solution.countPrimes(1500000)
# 114155

'''
题目：
计算小于非负数 n 的素数数。

分析：
从素数2开始，所有素数的倍数都不是素数，标记为0。
最后统计1的个数就是素数的个数。注意的是，re从0开始，0和1都不是素数，所以-2
'''