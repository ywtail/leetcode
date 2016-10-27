# coding:utf-8
# Pascal's Triangle 帕斯卡三角形

numRows=int(raw_input())

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    ans=[]
    for i in range(numRows):
        if i==0:
            ans.append([1])
        elif i==1:
            ans.append([1,1])
        else:
            temp=[1 for j in range(i+1)]
            for k in range(1,i):
                temp[k]=ans[i-1][k]+ans[i-1][k-1]
            ans.append(temp)
    return ans

print generate(numRows)

"""
5

[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

题目：
给定numRows，生成第一个num Pascal的三角形的行。
例如，给定numRows = 5，
返回[[1]，[1,1]，[1,2,1]，[1,3,3,1]，[1,4,6,4,1]]
"""