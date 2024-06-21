"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

e.g.
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""




class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        In-place: Means you cannot define such as nums2 and then let nums = nums2
        """
        # get the length of the array
        len_array = len(nums)

        # initialize a new pointer to identify the non-zero values
        non_zero_idx = 0

        for i in range(len_array):
            if nums[i] != 0:
                # if the current elem is not zero, move it to the non-zero index
                nums[non_zero_idx] = nums[i]
                # increment the non-zero index by 1
                non_zero_idx += 1


        # replace the last N elemns with 0, where (N = len_array - non_zero_idx)
        for i in range(non_zero_idx, len_array):
            nums[i] = 0

