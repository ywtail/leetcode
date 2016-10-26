# coding:utf-8
# Reverse Integer

x=int(raw_input())

def reverse(x):
    if x>=0:
        ans=int(str(x)[::-1])
    else:
        ans=-1*int(str(x)[:0:-1])
    m=2**31
    if ans<-m or ans>m: #超过整型范围，返回0
        return 0
    else:
        return ans

print reverse(x)

"""
-100

-1

题目：
整数的逆数字。
示例1：x = 123，返回321
示例2：x = -123，返回-321
"""