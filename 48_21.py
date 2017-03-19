# coding=utf-8
# 21.Merge Two Sorted Lists 合并两个排序链表
# 55ms,beats 70.51%

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newlist = ListNode(0)
        temp = newlist
        while (l1 and l2):
            if l1.val <= l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return newlist.next

# 将列表List转为链表ListNode
def createList(listnode, l):
    t = listnode
    for x in l:
        t.next = ListNode(x)
        t = t.next
    return listnode.next

# 为了方便测试，读取创建的链表ListNode每个节点的值
def readList(listnode):
    while listnode:
        print listnode.val,
        listnode = listnode.next
    print ""


l1 = map(int, raw_input().split())
l2 = map(int, raw_input().split())

list1 = ListNode(0)
list1 = createList(list1, l1)
readList(list1)

list2 = ListNode(0)
list2 = createList(list2, l2)
readList(list2)

solution = Solution()
ans = solution.mergeTwoLists(list1, list2)
readList(ans)

"""
题目：https://leetcode.com/problems/merge-two-sorted-lists/#/description
合并两个排序的链接列表，并将其作为新列表返回。 新列表应该通过将前两个列表的节点拼接在一起来进行。

题目本身很简单，对比两个链表当前的节点，哪个小就插入到newlist中。
"""
