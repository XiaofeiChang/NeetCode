"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

e.g.
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""



class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # initialize the maximum number of consecutive 1's in the array
        count_max = 0

        # initilize the number of consecutive 1's at the current position
        count = 0

        # iterate over the list to find the target number
        for n in nums:
            # increment the count to 1
            if n == 1:
                count = count + 1
                # check if the current count is larger than the max
                if count > count_max:
                    count_max = count
            # otherwise clear the count
            else:
                count = 0

        return count_max