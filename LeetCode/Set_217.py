""""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


# Hash Table solution see Hash_Table_217

# Defination:
# A set is an unordered collection of unique elements.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Hash Solution"""

        # # create a hash table (dictionary)
        # ht = {}

        # # iterate over the array
        # for key in nums:
        #     # if the key is alrealy in the dict
        #     if key in ht:
        #         # increment the value
        #         value = ht[key]
        #         value += 1
        #         # if the value is greater or equal to 2, return True
        #         if value >= 2:
        #             return True
        #         # otherwise, update the value of the key
        #         ht[key] = value

        #     # if not, add the new key into the dict
        #     else:
        #         ht[key] = 1

        # return False



        """Set Solution"""
        # copy to nums1
        nums1 = sorted(nums)

        # get the unique values by set func
        num_set = set(nums)
        # convert back from set to list type
        nums2 = sorted(list(num_set))

        # if not equal, contains duplication
        if nums1 != nums2:
            return True
        else:
            return False



