"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

e.g.
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
"""




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # The dummy = ListNode(0) line is used to handle cases where the head of the linked list (head) itself might need to be removed or modified.
        # The dummy node acts as a placeholder or starting point before the actual head.
        # Just be like a temp padding
        dummy = ListNode(0) # initialize a new node
        dummy.next = head # link the node to the linked list, before the beginning

        prev = dummy
        curr = dummy.next

        while curr:
            if curr.val == val:
                prev.next = curr.next

            else:
                prev = curr

            curr = curr.next

        # return dummy.next, which points to the head of the modified linked list
        return dummy.next