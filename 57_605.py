# coding:utf-8
# 605. Can Place Flowers 能种花吗
# 85ms beats 35.51%

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        t = 1
        for x in flowerbed:
            if count >= n:
                return True
            if x == 0:
                t += 1
            else:
                count += max(0, (t - 1) / 2)
                t = 0
        if t:
            count += t / 2
        if count >= n:
            return True
        else:
            return False


solution = Solution()
print solution.canPlaceFlowers([1, 0, 0, 0, 1], 1)
# True
print solution.canPlaceFlowers([1, 0, 0, 0, 1], 2)
# False
print solution.canPlaceFlowers([0, 1, 0, 0, 0, 1, 0, 0], 2)
# True
print solution.canPlaceFlowers([0, 0, 1, 0, 0, 0, 1, 0, 0], 3)
# True
print solution.canPlaceFlowers([0, 0, 0, 1, 0, 0, 0, 1, 0, 0], 4)
# False

'''
题目：
假设你有一个长的花坛，其中一些地块种植，有些不是。 然而，花不能种植在相邻的地块 - 他们会争夺水，两者都会死亡。
给定一个花坛（表示为0和1的数组，其中0表示空白，1表示不为空），数字n返回，如果n个新鲜花可以种植在其中，而不违反不相邻花规则。
示例1：
输入：flowerbed = [1,0,0,0,1]，n = 1
输出：True
示例2：
输入：flowerbed = [1,0,0,0,1]，n = 2
输出：False
注意：
1. 输入数组不会违反无相邻花规则。
2. 输入数组大小在[1，20000]的范围内。
3. n是不会超过输入数组大小的非负整数。

分析：
设连续的 0 的个数是 t，
在两端，则能种花的数量是：t/2
在中间，能种花的数量是：(t-1)/2，因为当 t==0 时，这个值是 -1，所以能种花的数量是 max(0, (t - 1) / 2)
两端和中间算法不同，为了代码简洁，可以手动给开头填充一个 0，从而利用 max(0, (t - 1) / 2) 这个计算公式。
填充方式是：t 初始置为 1

另一种做法是查看左右是否是 0，如果是就种一棵花。并把这里改为 1.
if(flowerbed[i] == 0) {
         //get next and prev flower bed slot values. If i lies at the ends the next and prev are considered as 0. 
               int next = (i == flowerbed.length - 1) ? 0 : flowerbed[i + 1]; 
               int prev = (i == 0) ? 0 : flowerbed[i - 1];
               if(next == 0 && prev == 0) {
                   flowerbed[i] = 1;
                   count++;
'''