"""

METHOD 1::::::::::


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



"""

METHOD 2::::::::::
BY CHATGPT




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


    
        # def update_min_root(node_temp):
        #     print("node_temp", node_temp)
        #     # The current smallest connected node must equals itself
        #     if parent[node_temp] == node_temp:
        #         return node_temp
        #     parent[node_temp] = update_min_root(parent[node_temp])
        #     print("parent", parent)
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:



        # find the **values in Dict** that are related to the node_temp
        def update_traversal_root(node_temp):
            update_key_node_list.append(node_temp)
            # The current smallest connected node must equals itself
            if parent[node_temp] != node_temp:
                update_traversal_root(parent[node_temp])
            return

        # find the **keys in dict** that are related to the node_temp
        def update_greater_traversal_root(node_temp):
            for key, val in parent.items():
                if val==node_temp or val==parent[node_temp]:
                    update_key_node_list.append(key)
            return


        """ N.B. The key idea to use both update_traversal_root() && and update_greater_traversal_root() is based on the constraints:
                *    edges[i] = [ai, bi]
                *    1 <= ai < bi <= edges.length
                *    ai != bi

            In 'parent' dictionary, we use the 'key' to represent the current node
                          use the 'value' to represent the smallest node that the current node could reach, named 'root' 


            As ai < bi, our 'value' <= 'key'


            We need to find both the keys equal to the current node, or the values equals to the current node, to update all nodes on the traversal.

        """



        parent = {}

        for e_pair in edges:
            # print(e_pair)
            node1 = e_pair[0]
            node2 = e_pair[1]

            if_node1 = (node1 in parent)
            if_node2 = (node2 in parent)

            # Case 1: ______________________________________________________________________
            if if_node1==False and if_node2==False:
                # print("Case 1")
                min_root = node1
                parent[node1] = min_root
                parent[node2] = min_root


            # Case 2: ______________________________________________________________________
            elif if_node1==True and if_node2==False:
                # print("Case 2")
                min_root = parent[node1]
                parent[node2] = min_root

            # Case 3: ______________________________________________________________________
            elif if_node1==False and if_node2==True:

                update_key_node_list = []

                if node1 < parent[node2]:
                    min_root = node1
                    parent[node1] = min_root

                    update_traversal_root(node2)
                    update_greater_traversal_root(node2)



                else:
                    min_root = parent[node2]
                    parent[node1] = min_root

                    update_traversal_root(node1)
                    update_greater_traversal_root(node1)

                # print("key node list", update_key_node_list)
                for key_node in update_key_node_list:
                    parent[key_node] = min_root


            # Case 4: ______________________________________________________________________
            elif if_node1==True and if_node2==True:
                # print("4")


                if parent[node1] == parent[node2]:
                    return e_pair



                else:
                    # min_root = min(parent[node1], parent[node2])
                    # parent[node1] = min_root
                    # parent[node2] = min_root



                    # if parent[node1] < parent[node2]:
                    #     min_root = parent[node1]
                    #     parent[node1] = min_root
                    #     parent[node2] = min_root
                    #     print(parent[node1], parent[node2])

                    #     update_min_root(node1)
                    #     update_min_root(node2)
                    # else:
                    #     min_root = parent[node2]
                    #     parent[node1] = min_root
                    #     parent[node2] = min_root

                    #     update_min_root(node2)
                    #     update_min_root(node1)

                    update_key_node_list = []

                    if parent[node1] < parent[node2]:
                        min_root = parent[node1]

                        update_traversal_root(node2)
                        update_greater_traversal_root(node2)



                    else:
                        min_root = parent[node2]

                        update_traversal_root(node1)
                        update_greater_traversal_root(node1)

                    # print("key node list", update_key_node_list)
                    for key_node in update_key_node_list:
                        parent[key_node] = min_root




            # print(parent)
            # print("___________________________________")





