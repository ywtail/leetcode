# coding:utf-8
# Pascal's Triangle II 帕斯卡三角形II

rowIndex=int(raw_input())

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    ans=[]
    for i in range(rowIndex+1):
        if i==0:
            ans.append([1])
        elif i==1:
            ans.append([1,1])
        else:
            temp=[1 for j in range(i+1)]
            for k in range(1,i):
                temp[k]=ans[i-1][k]+ans[i-1][k-1]
            ans.append(temp)
    return ans[rowIndex]

print getRow(rowIndex)

"""
3

[1, 3, 3, 1]

题目：
给定一个索引k，返回Pascal三角形的第n行。
例如，假设k = 3，
返回[1,3,3,1]。

注意：这里从第0行开始
"""