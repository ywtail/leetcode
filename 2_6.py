# coding:utf-8

s=raw_input()
numRows=int(raw_input())

def convert(s, numRows):
    if numRows==1:
    	return s
    else:
    	n=len(s)
    	ans=["" for i in range(numRows)] #存每一行的数据
    	p=0 #p标记s中当前位置
    	q=0 #q标记ans当前位置
    	while p<n: #按“之”字形往列表中存入数据
    		if q==0:
    			flag=1
    		if q==numRows:
    			flag=0
    			q=q-2
    		if flag: #读s中字符，从左往后存入ans中，ans=['P','A','Y']
    			ans[q]+=s[p]
    			p+=1
    			q+=1
    		else: #读s中字符，从右往左存入ans中，ans=['P','AP','Y']
    			if q>0:
    				ans[q]+=s[p]
    				p+=1
    				q-=1
    	return "".join(ans)

print convert(s, numRows)

"""
PAYPALISHIRING
3

PAHNAPLSIIGYIR

题目：
字符串“PAYPALISHIRING”以给定行数以之字形模式写入，如下所示：
P   A   H   N
A P L S I I G
Y   I   R
然后逐行读取：“PAHNAPLSIIGYIR”
编写代码，它将接受一个字符串，并使这个转换给出一定数量的行：
string convert（string text，int nRows）;
convert（“PAYPALISHIRING”，3）应返回“PAHNAPLSIIGYIR”。

分析：
对于s中的字符，先从左往右存入ans中，再从右往左追加到相应项中，以此类推。
具体见注释，在ans中存储：["PAHN","APLSIIG","YIR"]
P A Y
  P
A L I
  S
H I R
  I
N G
"""