# coding:utf-8
# Climbing Stairs 爬楼梯

n=int(raw_input())

def climbStairs(n):
	"""
	:type n: int
	:rtype: int
	"""
	if n==1:
		return 1
	else:
		ans=[1,1]
		for i in range(2,n+1):
			ans.append(ans[i-2]+ans[i-1])
		return ans[-1]

print climbStairs(n)

"""
题目：
你正在爬楼梯盒。 它需要n步到达顶部。
每次你可以爬1或2步。 你能爬到顶部有多少不同的方式？

分析：
方式[1,2,3,5,8,13,...]，从n=3开始，方式是前两项的和。
"""