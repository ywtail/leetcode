# coding:utf-8
# Add Binary 二进制数相加

a=raw_input()
b=raw_input()

def addBinary(a, b):
	"""
	:type a: str
	:type b: str
	:rtype: str
	"""
	lena=len(a)
	lenb=len(b)
	ans=""	
	if lena==0:
		ans=b
	elif lenb==0:
		ans=a
	else:
		flag=0
		if lenb>lena:
			lena,lenb=lenb,lena
			a,b=b,a
		for i in range(1,lenb+1):
			temp=int(a[lena-i])+int(b[lenb-i])+flag
			if temp>1:
				flag=1
				ans=str(temp-2)+ans
			else:
				flag=0
				ans=str(temp)+ans
		for j in range(lenb,lena):
			if flag==0:
				ans=a[:lena-j]+ans
				break
			else:
				temp=int(a[lena-j-1])+flag
				if temp>1:
					flag=1
					ans=str(temp-2)+ans
				else:
					flag=0
					ans=str(temp)+ans
		if flag==1:
			ans='1'+ans
	return ans

print addBinary(a, b)

"""
题目：
给定两个二进制字符串，返回它们的和（也是一个二进制字符串）。
例如，
a =“11”
b =“1”
返回“100”。
"""