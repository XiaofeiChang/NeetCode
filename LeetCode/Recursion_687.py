"""
Please see the example graph on the website: https://leetcode.com/problems/longest-univalue-path/description/
This problem is a little bit hard







Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.



Example 1:


Input: root = [5,4,5,1,1,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 5).
Example 2:


Input: root = [1,4,5,4,4,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 4).


Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
The depth of the tree will not exceed 1000.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
This solution might sum the edges among [root.prev, root.left, root.right], which does not satisfy the definition of a "path"







class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def recursion(curr_root, curr_len, max_len):

            # If the tree does not exist
            if not curr_root:
                return max_len

            print("Node:", curr_root.val, "curr_len", curr_len, "max_len", max_len)


            root_val = curr_root.val
            if curr_root.left: 
                left_val = curr_root.left.val 
                if root_val==left_val:
                    curr_len += 1

                else:
                    curr_len = 0

            max_len = max(max_len, curr_len)       



            if curr_root.right: 
                right_val = curr_root.right.val 
                if root_val==right_val:
                    curr_len += 1

                else:
                    curr_len = 0
            print(max_len,curr_len)
            max_len = max(max_len, curr_len)     

            max_len = recursion(curr_root.left, curr_len, max_len)

            max_len = recursion(curr_root.right, curr_len, max_len)
            print(max_len,curr_len)


            return max_len



        # If the tree does not exist at all
        if not root:
            return 0

        # Initialization
        max_len = 0  # the longest path
        initial_root_len = 0 # the initial number of continuous path
        initial_root_val = root.val
        # recursion(prev_val = initial_root_val, curr_len=initial_root_len)
        max_len = recursion(curr_root=root, curr_len=initial_root_len, max_len=max_len)

        return max_len
        """









""" 
The below method reach the bottom of the tree first before summing up anything. 

It always 
        (sum the left&right to find the max), 
        &&
        (preserve one of the branch by "return max(curr_L_len, curr_R_len)""), 

These operations avoid the case metioned in the above solution.
"""


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def recursion(curr_root):
            # We firstly reach the bottom
            if not curr_root:
                return 0

            curr_L_len = recursion(curr_root.left)
            curr_R_len = recursion(curr_root.right)

            root_val = curr_root.val
            if curr_root.left:
                left_val = curr_root.left.val
                if root_val == left_val:
                    curr_L_len += 1
                else:
                    curr_L_len = 0

            if curr_root.right:
                right_val = curr_root.right.val
                if root_val == right_val:
                    curr_R_len += 1

                else:
                    curr_R_len = 0

            self.max_len = max(self.max_len, curr_L_len + curr_R_len)

            # Each recursive call returns the longest path length (either left or right, whichever is greater) that can be extended by its parent.
            # Also to avoid the case metioned in the above solution
            return max(curr_L_len, curr_R_len)

        # If the tree does not exist at all
        if not root:
            return 0
        self.max_len = 0
        recursion(curr_root=root)

        return self.max_len