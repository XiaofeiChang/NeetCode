"""Given an integer array nums, find the subarray with the largest sum, and return its sum."""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """


        A slower method.





        # Case 1:
        if len(nums)==1:
            return nums[0]


        # Case 2:
        # The case that all numbers < 0
        isPositiveExist = False

        # Initialize the pointers with the first positive value for case 3
        L, R = 0, 0
        for i in range(len(nums)):
            if nums[i]>0:
                L,R = i,i
                isPositiveExist = True
                break

        # if isPositiveExist=False, which means all elems <= 0, directly return the max value
        if isPositiveExist==False:
            return max(nums)




        # Case 3:
        # Initialize the result
        max_sum = 0

        # Find the subarray with the largest sum:
        # As long as the current sum > 0, keep ascending the R pointer
        # Once the current sum <=0, move the L to the current R index, as the current sum of nums[L:R] would only decrease the result
        while R<len(nums):
            # Note: slice end index should be R+1 because the end index is exclusive in Python slices
            curr_sum = sum(nums[L:R+1])

            if curr_sum > 0:
                max_sum = max(max_sum, curr_sum)
            else:
                # Move the pointers
                L = R+1

            # Ascending
            R = R+1

        return max_sum"""






        # Kadane's Algorithm:

        if not nums:
            return 0

        # Initialize current sum and max sum found so far.
        current_sum = max_sum = nums[0]

        # Start iterating from the second element since the first is already used to initialize.
        for num in nums[1:]:
            # If current sum is negative, it's better to restart the subarray with the current element
            current_sum = max(num, current_sum + num)
            # Update the max sum found so far
            max_sum = max(max_sum, current_sum)

        return max_sum


