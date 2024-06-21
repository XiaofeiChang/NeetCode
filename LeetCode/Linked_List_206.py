"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

e.g.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is none or if there is only a head in the linked list
        if not head or not head.next:
            return head

        prev = None
        curr = head

        while curr:
            # store the node of curr.next
            temp = curr.next
            # reverse
            curr.next = prev
            # update
            prev = curr
            curr = temp

        return prev