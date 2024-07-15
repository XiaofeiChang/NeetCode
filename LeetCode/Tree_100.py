"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # No need to create or pass any initialized variable, therefore no need the nested function like Tree_144 or Tree_589

        # N.B. all these three cases are for recursive check

        # Case 1: both None
        if (p is None) and (q is None):
            return True

        # Case 2: only one is none
        elif (p is None) or (q is None):
            return False

        # Case 3: No none, check each node value
        if p.val != q.val:
            return False

        # Organize the results in each recursion to get the final result
        bool1 = self.isSameTree(p.left, q.left)
        bool2 = self.isSameTree(p.right, q.right)
        return bool1 and bool2  # Once there is a False case during the recursion, the 'and' operation will return false