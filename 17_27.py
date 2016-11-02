# coding:utf-8
# Remove Element 删除元素

nums=map(int,raw_input().split())
val=int(raw_input())

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    n=len(nums)
    p=0
    for i in range(n):
    	if nums[p]==val:
    		del nums[p]
    	else:
    		p+=1
    return p

print removeElement(nums, val)

"""
3 2 3 4
3

2

题目：
给定数组和值，原位删除该值的所有实例，并返回新长度。
不要为另一个数组分配额外的空间，必须使用常量内存来做到这一点。
可以更改元素的顺序。超出了新的长度也没有关系。
例：
给定输入数组nums = [3,2,2,3]，val = 3
您的函数应返回length = 2，num的前两个元素为2。
暗示：
尝试两个指针。
你使用了属性“元素的顺序可以改变”吗？
当要删除的元素很少时会发生什么？
"""