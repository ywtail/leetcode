# coding:utf-8
# Add Strings 字符串相加

num1=raw_input()
num2=raw_input()

def addStrings(num1,num2):
	"""
    :type num1: str
    :type num2: str
    :rtype: str
    """
	n1=len(num1)
	n2=len(num2)
	if n1==0:
		ans=num2
	elif n2==0:
		ans=num1
	else:
		if n1<n2:
			n1,n2=n2,n1
			num1,num2=num2,num1

		ans=""
		flag=0
		for i in range(1,n2+1):
			temp=int(num1[n1-i])+int(num2[n2-i])+flag
			if temp>9:
				flag=1
				ans=str(temp-10)+ans
			else:
				flag=0
				ans=str(temp)+ans
		for j in range(n2,n1):
			if flag==0:
				ans=num1[:(n1-j)]+ans
				break
			else:
				temp=int(num1[n1-j-1])+flag
				if temp>9:
					flag=1
					ans=str(temp-10)+ans
				else:
					flag=0
					ans=str(temp)+ans
		if flag==1:
			ans='1'+ans
	return ans				

print addStrings(num1,num2)

"""
99
9

108

题目：
给定两个非负数num1和num2表示为字符串，返回num1和num2的和。
注意：
num1和num2的长度都小于5100。
num1和num2只包含数字0-9。
num1和num2都不包含任何前导零。
您不能使用任何内置的BigInteger库或直接将输入转换为整数。
"""