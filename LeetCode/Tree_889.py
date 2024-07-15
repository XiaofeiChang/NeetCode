"""
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.



Example 1:


Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]


Constraints:

1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.

"""


"""
This method could only return the tree node in a List type but not TreeNone, therefore this is not accepted






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def getRoot(tree):
            if len(tree) == 0:
                return

            # empty it for new recursion
            temp_subtrees = []

            for t in tree:
                t_len = len(t)

                root = t[0]
                result.append(root)

                # if the current node is the leaf of the tree
                if t_len == 1:
                    continue

                left_subtree = t[1: round(t_len / 2)]
                right_subtree = t[round(t_len / 2):]

                # Case1: the current node is not the leaf of the tree
                if len(left_subtree) >= 1:
                    temp_subtrees.append(left_subtree)
                if len(right_subtree) >= 1:
                    temp_subtrees.append(right_subtree)

            getRoot(temp_subtrees)

        result = []


        # '''
        # for each subtree::
        #
        # root: subtree[0]
        # left: subtree[1: round(len(subtree)/2)]
        # right: subtree[round(len(subtree)/2): ]
        # '''


        root0 = preorder[0]
        left_subtree = preorder[1: round(len(preorder) / 2)]
        right_subtree = preorder[round(len(preorder) / 2):]
        temp_subtrees = [left_subtree, right_subtree]

        result.append(root0)
        getRoot(temp_subtrees)

        return result


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    ### N.B. The main idea is based on index calculation of binary tree

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def getRoot(tree):
            if len(tree) == 0:
                return

            # empty it for new recursion
            temp_subtrees = []

            for t in tree:
                t_len = len(t)

                root = t[0]
                result.append(root)

                # if the current node is the leaf of the tree
                if t_len == 1:
                    continue

                left_subtree = t[1: round(t_len / 2)]
                right_subtree = t[round(t_len / 2):]

                # Case1: the current node is not the leaf of the tree
                if len(left_subtree) >= 1:
                    temp_subtrees.append(left_subtree)
                if len(right_subtree) >= 1:
                    temp_subtrees.append(right_subtree)

            getRoot(temp_subtrees)

            return result

        # Construct the TreeNodes by using the result List
        def constructTree(result_reindex, idx):

            bound = len(result_reindex) - 1
            print(bound, 2 * idx + 1)

            # terminate condition
            # You need to iterate over each node in the list, as the none is also needed to be constructed
            if idx > bound:
                return None

            curr_node = result_reindex[idx]
            root = TreeNode(curr_node)

            left_node_idx = 2 * idx
            right_node_idx = 2 * idx + 1
            root.left = constructTree(result_reindex, left_node_idx)
            root.right = constructTree(result_reindex, right_node_idx)
            return root

        # Deal with 2 special cases
        if len(preorder) == 0:
            return []

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        result = []
        """
        for each subtree::

        root: subtree[0]
        left: subtree[1: round(len(subtree)/2)]
        right: subtree[round(len(subtree)/2): ]
        """
        # Step1: Get the result(output) in List Type
        root0 = preorder[0]
        left_subtree = preorder[1: round(len(preorder) / 2)]
        right_subtree = preorder[round(len(preorder) / 2):]
        temp_subtrees = [left_subtree, right_subtree]

        result.append(root0)

        result = getRoot(temp_subtrees)

        # Step2: Convert the result to the Tree Type
        # Insert a 0 at the beginning to  re-index
        result.insert(0, 0)
        result_tree = constructTree(result,
                                    idx=1)  # the root of the tree is with value 1 at the idx=1 in the reindexed result list

        return result_tree