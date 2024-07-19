"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4



"""















"""
# This method might be wrong as it might skip some index
# curr_idx = round((left + right)/2):

# round() function: This approach uses the round() function, which rounds the result of the division to the nearest integer. If the fractional part of the number is 0.5 or greater, it rounds up; otherwise, it rounds down.
# Example: If left = 0 and right = 3, then round((0 + 3) / 2) evaluates to round(1.5), which is 2.

# curr_idx = (left + right) // 2:

# Integer division (//): This approach uses integer division, which always rounds down to the nearest integer, regardless of the fractional part.
# Example: If left = 0 and right = 3, then (0 + 3) // 2 evaluates to 1.





class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Special Case 0: if there is only 1 number in nums and it is right the target
        if nums[0]==target:
            return 0
        # Special Case 1: target smaller than nums[0]
        if target < nums[0]:
            return 0
        # Special Case 2: target greater than nums[-1]
        if target > nums[-1]:
            return len(nums)

        # Initialize two pointers:
        left = 0
        right = len(nums) - 1

        while left <= right:

            curr_idx = round((left + right)/2)
            curr = nums[curr_idx]
            print(left, right, "mid=", curr_idx)

            if target == curr:
                print("3")
                return curr_idx

            if target < curr:
                print("1")
                # move the pointer
                right = curr_idx - 1

            elif target > curr:
                print("2")
                # move the pointer
                left = curr_idx + 1

        return left




"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Special Case 0: if there is only 1 number in nums and it is right the target
        if nums[0] == target:
            return 0
        # Special Case 1: target smaller than nums[0]
        if target < nums[0]:
            return 0
        # Special Case 2: target greater than nums[-1]
        if target > nums[-1]:
            return len(nums)

        # Initialize two pointers:
        left = 0
        right = len(nums) - 1

        while left <= right:

            curr_idx = (left + right) // 2
            curr = nums[curr_idx]
            print(left, right, "mid=", curr_idx)

            if target == curr:
                print("3")
                return curr_idx

            if target < curr:
                print("1")
                # move the pointer
                right = curr_idx - 1

            elif target > curr:
                print("2")
                # move the pointer
                left = curr_idx + 1

        return left


"""A simpler version: No need to think about the special case



class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # Initialize two pointers:
        left = 0
        right = len(nums) - 1

        while left <= right:

            curr_idx = (left + right)//2
            curr = nums[curr_idx]
            print(left, right, "mid=", curr_idx)

            if target == curr:
                print("3")
                return curr_idx

            if target < curr:
                print("1")
                # move the pointer
                right = curr_idx - 1

            elif target > curr:
                print("2")
                # move the pointer
                left = curr_idx + 1

        return left

"""