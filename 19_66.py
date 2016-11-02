# coding:utf-8
# Plus One 加一

digits=map(int,raw_input().split())

def plusOne_1(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    ans=[]
    for x in str(int("".join(map(str,digits)))+1):
    	ans.append(int(x))
    return ans

def plusOne_2(digits):
	n=len(digits)
	p=n-1
	tag=0
	for i in range(n+1):
		temp=digits[p]+1
		if temp<10:
			digits[p]=temp
			return digits
		else:
			digits[p]=temp-10
			p-=1
		if p==-1:
			digits.insert(0,1)
			return digits

print plusOne_1(digits)
print plusOne_2(digits)

"""
9 9

[1, 0, 0]
[1, 0, 0]

题目：
给定一个表示为数字数组的非负数，加上一。
存储数字，使得最高有效数字在列表的头部。

分析：
题目的意思是：给出一个列表，这个列表中有多个整数，连起来是一个整数，要对这个整数+1，
并且将得到的结果的每一位作为列表的每一项。
方法一：
将输入列表转成整数+1，,然后将结果转成字符串，将字符串的每一位转成整数append到结果列表中。
方法二：
从后往前遍历输入列表，检测有没有进位。
"""