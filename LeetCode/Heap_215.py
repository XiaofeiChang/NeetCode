"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        # If you directly sort it by heaoipy, you may get [1, 2, 3, 5, 6, 4] when k=2
        # Therefore the following method is incorrect

        heapq.heapify(nums)
        print(nums)
        num = nums[-k]
        return num
        """


        """"
        *** heap property. 
                In a min-heap, for any given node i, the value of i is less than or equal to the values of its children, which ensures that the smallest element is always at the root of the heap. 
                Conversely, in a max-heap, the value of i is greater than or equal to the values of its children, ensuring the largest element is at the root.
                
                N.B. To make everything work, the heap array indexing from 1 for built-in counting
                        e.g. In nums = [3, 2, 1, 5, 6, 4], the index 2 is element '2'
                        
                        left child idx = 2*idx
                        right chile idx = 2*idx + 1
                        parent idx = idx / 2

        
        
        *** Example of Heap Operations
                
        
                Consider the array nums = [3, 2, 1, 5, 6, 4] and converting it to a min-heap:
                
                Initial Array: [3, 2, 1, 5, 6, 4]
                
                Heapify Operation:
                
                Starting from the middle of the array and moving backwards to ensure that each subtree satisfies the heap property:
                The subtree rooted at index 2 (1, 5, 6, 4) already satisfies the heap property.
                The subtree rooted at index 1 (2, 5, 6, 4) already satisfies the heap property.
                The subtree rooted at index 0 (3, 2, 1, 5, 6, 4) is modified to [1, 2, 3, 5, 6, 4].
                
                
            
                
                
                
        *** Why Heaps Cannot Directly Sort an Array
                The primary purpose of a heap is to efficiently find the smallest (or largest) element. While heaps are great for specific operations, they are not designed for sorting the entire array in a single operation. Here's why:
                
                Heap Property Maintenance:
                
                Heaps maintain a specific order property (either min or max), which does not translate directly to a fully sorted order.
                Partial Order:
                
                A heap only guarantees that the root is the smallest (or largest) element and that the subtree properties are maintained, but it does not provide a global ordering of all elements.
                Sorting with Heaps:
                
                You can use a heap to sort an array by repeatedly removing the smallest element and rebuilding the heap (heap sort), but this involves multiple heap operations (logarithmic complexity each time), rather than a single reorganization.
        """

        # Create a min-heap with the first k elements
        hp = nums[:k]
        heapq.heapify(hp)

        for num in nums[k:]:
            # If the current element is larger than the smallest in the heap
            if num>hp[0]:
                heapq.heapreplace(hp, num) # Replace and re-heapify
        # The root of the heap is the k-th largest element
        return hp[0]