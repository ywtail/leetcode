# coding:utf-8
# Rotate Function 旋转函数

A=map(int,raw_input().split())

def maxRotateFunction(A):
	"""
	:type A: List[int]
	:rtype: int
	"""
	n=len(A)
	s=sum(A)
	F0=0
	for i in range(n):
		F0+=(i*A[i])
	F=[F0]
	ma=F0
	for i in range(1,n):
		temp=F[i-1]+s-n*A[-i]
		F.append(temp)
		if temp>ma:
			ma=temp
	return ma

print maxRotateFunction(A)

"""
1 2 3 4 5 6 7 8 9 10

330

题目：
https://leetcode.com/problems/rotate-function/
给定一个数组A，令n为其长度。
假设Bk是通过按顺时针旋转数组A k获得的数组，我们在A上定义A的“旋转函数”F如下：
F（k）= 0 * Bk [0] + 1 * Bk [1] + ... +（n-1）* Bk [n-1]。
计算F（0），F（1），...，F（n-1）的最大值。
注意：
n保证小于10^5。
例：
A = [4,3,2,6]
F（0）=（0×4）+（1×3）+（2×2）+（3×6）= 0 + 3 + 4 + 18 = 25
F（1）=（0×6）+（1×4）+（2×3）+（3×2）= 0 + 4 + 6 + 6 = 16
F（2）=（0 * 2）+（1 * 6）+（2 * 4）+（3 * 3）= 0 + 6 + 8 + 9 = 23
F（3）=（0×3）+（1×2）+（2×6）+（3×4）= 0 + 2 + 12 + 12 = 26
因此F（0），F（1），F（2），F（3）的最大值为F（3）= 26。

分析：
找F(i)和F(i+1)之间的规律，就不需要每次都遍历了。
F(i+1)=F(i)+sum(A)-n*A[-(i+2)]
"""