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
		temp=l1.val+l2.val
		anslist=ListNode(temp%10)
		tag=temp/10
		l1=l1.next
		l2=l2.next
		t=anslist
		while l1 and l2:
			temp=l1.val+l2.val+tag
			t.next=ListNode(temp%10)
			t=t.next
			tag=temp/10
			l1=l1.next
			l2=l2.next
		while l1:
			temp=l1.val+tag
			t.next=ListNode(temp%10)
			t=t.next
			tag=temp/10
			if tag==0:
				t.next=l1.next
				break
			l1=l1.next
		while l2:
			temp=l2.val+tag
			t.next=ListNode(temp%10)
			t=t.next
			tag=temp/10
			if tag==0:
				t.next=l2.next
				break
			l2=l2.next
		if tag:
			t.next=ListNode(tag)

		"""
		# 为了测试结果是否正确
		k=0
		z=0
		while anslist:
			z=z+anslist.val*(10**k)
			anslist=anslist.next
			k+=1
		print z
		"""

		return anslist

arr1=[1,2,4]
arr2=[9,1,6,9,9,9]

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
使用了3个while，比46_m_2_1.py更慢。
"""