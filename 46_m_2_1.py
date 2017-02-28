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
		a=0
		i=0
		while(l1):
			a=a+l1.val*(10**i)
			l1=l1.next
			i+=1
		#print a
		b=0
		j=0
		while(l2):
			b=b+l2.val*(10**j)
			l2=l2.next
			j+=1
		#print b
		ans=a+b
		anslist=ListNode(ans%10)
		ans/=10
		anstemp=anslist
		while ans>0:
			anstemp.next=ListNode(ans%10)
			anstemp=anstemp.next
			ans/=10
		
		"""
		# 为了测试结果是否正确
		k=0
		t=0
		while anslist:
			t=t+anslist.val*(10**k)
			anslist=anslist.next
			k+=1
		print t
		"""

		return anslist

arr1=[1,2,4]
arr2=[9,1,5,6]

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

将链表转换成整数（反序），整数求和之后将整数转换成链表
"""