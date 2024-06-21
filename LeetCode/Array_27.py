"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.

Return k.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""




class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # get the length of nums
        len_nums = len(nums)

        # initialize a new pointer to identify the non-val values.
        non_val_idx = 0

        # iterate over the nums array
        for i in range(len_nums):
            if nums[i] != val:
                # if the current elem is not equal to val, move it to the non-val index
                nums[non_val_idx] = nums[i]
                # increment the index by 1
                non_val_idx += 1

        for i in range(non_val_idx, len_nums):
            # replace the rest of elements with placeholders
            nums[i] = None

        # get the number of non_val elements
        k = non_val_idx

        return k