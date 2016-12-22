# coding:utf-8
# 412. Fizz Buzz

n=int(raw_input())

def fizzBuzz(n):
	"""
	:type n: int
	:rtype: List[str]
	"""
	ans=[str(i) for i in range(1,n+1)]
	for i in range(1,n/3+1):
		ans[i*3-1]="Fizz"
	for j in range(1,n/5+1):
		ans[j*5-1]="Buzz"
	for k in range(1,n/15+1):
		ans[k*15-1]="FizzBuzz"
	return ans

print fizzBuzz(n)

"""
编写一个输出数字从1到n的字符串表示形式的程序。
但是对于三的倍数，
应该输出“Fizz”而不是数字和五个输出“Buzz”的倍数。 
对于三个和五个输出“FizzBuzz”的倍数的数字。
Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""