# LeetCode
# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
curr : 1->2->3->4->5
prev : None
next : 2->3->4->5

curr.next = prev
(curr : 1->None)

prev,curr = curr,next
(prev : 1->None)
(curr : 2->3->4->5)
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head node를 curr라고 하고, None을 prev라고 설정 
        curr, prev = head, None
        while curr:
            # next는 다음에 옮길 node를 나타냄
            # 다음 node에 prev를 넣어줌 
            next, curr.next = curr.next, prev
            # 현재 옮긴 node를 prev로, 다음에 옮길 node를 curr라고 설정 
            prev, curr = curr, next
        return prev
