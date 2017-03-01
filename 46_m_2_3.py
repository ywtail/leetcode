# coding=utf-8
# 2. Add Two Numbers

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		anslist=ListNode(0)
		temp=anslist
		s=0
		i=0
		while l1 or l2:
			if l1:
				s+=l1.val
				l1=l1.next
			if l2:
				s+=l2.val
				l2=l2.next
			temp.next=ListNode(s%10)
			temp=temp.next
			s=s/10 #充当tag
		if s:
			temp.next=ListNode(s)
		
		"""
		# 测试结果是否正确
		anslist=anslist.next #最开始的0不打印
		while(anslist):
			print anslist.val,
			anslist=anslist.next
		"""

		return anslist.next

arr1=[1,2,4]
arr2=[9,1,6,9]

l1=ListNode(arr1[0])
temp1=l1
for x in arr1[1:]:
	temp1.next=ListNode(x)
	temp1=temp1.next

l2=ListNode(arr2[0])
temp2=l2
for x in arr2[1:]:
	temp2.next=ListNode(x)
	temp2=temp2.next

s=Solution()
s.addTwoNumbers(l1,l2)

"""
题目：
您将获得两个非空链接列表，表示两个非负整数。 数字以相反的顺序存储，并且它们的每个节点包含单个数字。 添加两个数字并将其作为链接列表返回。
您可以假定这两个数字不包含任何前导零，除了数字0本身。
输入：（2→4→3）+（5→6→4）
输出：7→0→8

逐一将相对应位置的数相加，加到链表。
比2快，代码简洁，然而依然没有1快。
"""