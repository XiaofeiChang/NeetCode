"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.



Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]




Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]



 Example 3:


Input: edges = [[3,4],[1,2],[2,4],[3,5],[2,5]]
Output: [2,5]



Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""







"""
        This method is not work, this rule is designed by observising the given cases, but it can not deal with::
        **
        Input edges =
        [[3,4],[1,2],[2,4],[3,5],[2,5]]
        **
        Use Output
        [2,4]
        **
        Expected
        [2,5]




        # Initialize a set to save the visited nodes (distinct)
        visited_nodes = set()
        # Initialize the result
        redundant_edge = 0

        for e_pair in edges:
            node1 = e_pair[0]
            node2 = e_pair[1]
            # check if the nodes has already been visited
            # if both of them have been visited, return the current edge as the result
            if (node1 in visited_nodes) and (node2 in visited_nodes):
                redundant_edge = e_pair
                break

            # Otherwise, append the nodes to the set. N.B. As set() only store distinct elements, no matter the nodes has been appended or not, just implement the following operation.
            else:
                visited_nodes.add(node1)
                visited_nodes.add(node2)

        return redundant_edge
        """


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # # Dictionary to keep track of the parent of each node
        # parent = {}

        # # Helper function to find the root of a node with path compression
        # def find(x):
        #     if parent[x] != x:
        #         parent[x] = find(parent[x])  # Path compression

        #     return parent[x]

        # # Helper function to union two nodes
        # def union(x, y):
        #     rootX = find(x)
        #     rootY = find(y)
        #     if rootX != rootY:
        #         parent[rootX] = rootY  # Union the roots
        #         return True
        #     print(parent)
        #     return False  # Return False if x and y are already connected

        # # Process each edge in the graph
        # for u, v in edges:
        #     if u not in parent:
        #         parent[u] = u  # Initialize the parent of u to itself
        #     if v not in parent:
        #         parent[v] = v  # Initialize the parent of v to itself
        #     if union(u, v) is False:
        #         return [u, v]  # Return the edge if it forms a cycle

        parent = {}

        for e_pair in edges:
            node1 = e_pair[0]
            node2 = e_pair[1]

            if_node1 = (node1 in parent)
            if_node2 = (node2 in parent)

            if if_node1 == False and if_node2 == False:
                print("1")
                min_root = node1
                parent[node1] = min_root
                parent[node2] = min_root

            elif if_node1 == True and if_node2 == False:
                print("2")
                min_root = parent[node1]
                parent[node2] = min_root

            elif if_node1 == False and if_node2 == True:
                print("3")
                min_root = min(node1, parent[node2])
                parent[node1] = min_root
                parent[node2] = min_root

            elif if_node1 == True and if_node2 == True:
                print("4")
                # check if the current min roots are all 1
                len_parent = len(parent)
                sum_min_root = sum(parent.values())
                if len_parent == sum_min_root:
                    return e_pair
                else:
                    min_root = min(parent[node1], parent[node2])
                    parent[node1] = min_root
                    parent[node2] = min_root
            print(parent)





