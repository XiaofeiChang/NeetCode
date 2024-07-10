"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.


Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.








# For visualized graph, please see the original page on leetcode website



"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        # This method is not work, may fall into infite loop such as :

        curr_node: 3,  temp_curr_node:2
        curr_node: 3,  temp_curr_node:0
        curr_node: 3,  temp_curr_node:-4
        curr_node: 3,  temp_curr_node:2
        curr_node: 3,  temp_curr_node:0
        curr_node: 3,  temp_curr_node:-4
        curr_node: 3,  temp_curr_node:2
        curr_node: 3,  temp_curr_node:0
        , whose
            head =
            [3,2,0,-4]
            pos =
            1






        # If the linked list is None, directly return false
        if head is None:
            return False


        # Initialize the result
        is_cycle = False


        # initialize the current node and the next node:  curr_node = head
        curr_node = head

        # Iterate over the entire linkedlist by using dummy to point each list node one by one
        while curr_node:
            # Get the temp_curr_node to implement the inner loop
            temp_curr_node = curr_node.next
            # while the temp_curr_node is not none
            while temp_curr_node:
                print("curr_node: " + str(curr_node.val) + ",  temp_curr_node:" + str(temp_curr_node.val))
                # if there is a following pointer pointing to the current node
                if temp_curr_node == curr_node:
                    is_cycle = True
                    break # Break out of the inner loop

                # check the next
                temp_curr_node = temp_curr_node.next

            # Break out of the outer loop
            if is_cycle == True:
                break

            # check the next
            curr_node = curr_node.next

        return is_cycle"""





        # Basic idea:  If there is a cycly, the stepsize-2 pointer (fast) will always meet stepsize-1 pointer finally
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True





