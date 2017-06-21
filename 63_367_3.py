# coding:utf-8
# 367. Valid Perfect Square 有效的完美平方
# 55ms beats 20.27%

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        while x * x > num:
            x = (x + num / x) / 2
        return x * x == num


solution = Solution()
print solution.isPerfectSquare(16)
# True
print solution.isPerfectSquare(8)
# False

'''
题目：
给定一个正整数num，写一个函数返回True，如果num是一个完美的平方，否则返回False。
注意：不要使用任何内置的库函数，如sqrt。
示例1：
输入：16
返回值：True
示例2：
输入：14
返回：False

分析：
牛顿法：http://www.matrix67.com/blog/archives/361
> 首先随便猜一个近似值x，然后不断令x等于x和a/x的平均数，迭代个六七次后x的值就已经相当精确了。
我们仅仅是不断用(x,f(x))的切线来逼近方程x^2-a=0的根。
根号a实际上就是x^2-a=0的一个正实根，这个函数的导数是2x。
也就是说，函数上任一点(x,f(x))处的切线斜率是2x。
那么，x-f(x)/(2x)就是一个比x更接近的近似值。
代入f(x)=x^2-a得到x-(x^2-a)/(2x)，也就是(x+a/x)/2。
'''