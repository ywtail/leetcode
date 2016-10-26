# coding:utf-8
# Palindrome Number

x=int(raw_input())

def isPalindrome(x):
    if x<0: #负数返回False
        return False
    elif x>=0 and x<10: #1位数返回True
        return True
    else:
        s=str(x)
        p=0
        q=len(s)-1
        while p<q: #p“指针”从前往后，q“指针”从后往前，只要不相等就返回False
            if s[p]!=s[q]:
                return False
            p+=1
            q-=1
        return True

print isPalindrome(x)

"""
100

False

题目：
确定整数是否是回文。 不提供额外的空间。
"""