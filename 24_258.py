# coding:utf-8
# Add Digits （每一位）数字相加

num=int(raw_input())

def addDigits(num):
	"""
	:type num: int
	:rtype: int
	"""
	if num==0: #因为num==0时，-1%9=8，所以单独讨论
		ans=0
	else:
		ans=(num-1)%9+1
	return ans
	
print addDigits(num)

"""
18

9

题目：
给定一个非负整数num，重复添加所有其数字，直到结果只有一个数字。
例如：
给定num = 38，过程如下：3 + 8 = 11,1 + 1 = 2。由于2只有一个数字，返回它。
跟进：
你能让它没有任何循环/递归在O（1）运行时？
提示：
上述过程的实现是微不足道的。 你能想出其他方法吗？
所有可能的结果是什么？
它们如何发生，定期或随机？
您可能会发现这篇维基百科文章有用：https://en.wikipedia.org/wiki/Digital_root

分析：
这种做法叫digital root或者repeated digital sum
if n=0,dr(n)=0
elif n%9==0,dr(n)=9
else dr(n)=n%9
总结：dr(n)=mod(n-1,9)+1
一个数x的数根为mod(x-1,9)+1。
因为正整数对9取模的结果取值为[0,8],而数根的取值为[1,9]。
"""