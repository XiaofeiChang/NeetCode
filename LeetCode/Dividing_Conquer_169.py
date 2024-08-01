"""
For explanation, please refer to: Notes for Questions/DIviding_Conquer_169.png



Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


"""


class Solution:
    def majorityElement(self, nums):
        # Define the recursive function based on segment tree (dividing&conquer) to find the majority element
        # All the returned values are a certain number in nums
        def recursion(start, end):
            # When reach the bottom of the tree, we return its value in num
            if start == end:
                majority = nums[start]
                return majority

            # Step 1(Dividing): Segment Tree Spliting
            mid = (start + end) // 2
            left_majority = recursion(start, mid)
            right_majority = recursion(mid + 1, end)

            # Step 2(Conquer): Compare to find the majority

            # Case 1: left and right majorities equal, return any one of them
            if left_majority == right_majority:
                majority = left_majority
                return majority

            # Case 2: not equal values, need to compare the counts
            else:
                # Left
                left_majority_count = 0
                for i in range(start, end + 1):
                    if nums[i] == left_majority:
                        left_majority_count += 1

                # Right
                right_majority_count = 0
                for i in range(start, end + 1):
                    if nums[i] == right_majority:
                        right_majority_count += 1

                # Return the majority with larger count, there actually no 'left_majority_count = right_majority_count' case as it has been handled at Case 1
                if left_majority_count > right_majority_count:
                    majority = left_majority
                else:
                    majority = right_majority
                return majority

        start0 = 0
        end0 = len(nums) - 1
        majority = recursion(start0, end0)
        return majority

