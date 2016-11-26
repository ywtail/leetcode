# coding:utf-8
# Rectangle Area 矩形区域

A=int(raw_input())
B=int(raw_input())
C=int(raw_input())
D=int(raw_input())
E=int(raw_input())
F=int(raw_input())
G=int(raw_input())
H=int(raw_input())

def computeArea(A, B, C, D, E, F, G, H):
	"""
	:type A: int
	:type B: int
	:type C: int
	:type D: int
	:type E: int
	:type F: int
	:type G: int
	:type H: int
	:rtype: int
	"""
	ans=(C-A)*(D-B)+(G-E)*(H-F)
	if C<=E or G<=A or H<=B or D<=F:
		return ans
	else:
		t=(min(G,C)-max(A,E))*(min(D,H)-max(B,F))
		return ans-t

print computeArea(A, B, C, D, E, F, G, H)

"""
题目：
https://leetcode.com/problems/rectangle-area/
找到2D平面中的两个直线矩形覆盖的总面积。
每个矩形由其左下角和右上角定义，如图所示。
假设总面积从不超过int的最大可能值。
"""