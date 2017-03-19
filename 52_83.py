# coding=utf-8
# 83. Remove Duplicates from Sorted List 从排序列表中删除重复项
# 85ms beats 13.72%

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        now = head
        if not head:
            return head
        while now.next:
            if now.val == now.next.val:
                now.next = now.next.next
                #now = now.next 这句不能要，如果有则[1,1,1]输出[1,1]
            else:
                now = now.next
            if not now: #important
                break
        return head


def createList(listNode, l):
    temp = listNode
    for k in l:
        temp.next = ListNode(k)
        temp = temp.next
    return listNode.next


def readList(listNode):
    while listNode:
        print listNode.val,
        listNode = listNode.next
    print ""


l = map(int, raw_input().split())
listnode = ListNode(0)
listnode = createList(listnode, l)
# readList(listnode)

solution = Solution()
readList(solution.deleteDuplicates(listnode))

'''
给定一个排序的链表，删除所有重复，使每个元素只出现一次。
例如，
给定1-> 1-> 2，返回1-> 2。
给定1-> 1-> 2-> 3-> 3，返回1-> 2-> 3。
'''
