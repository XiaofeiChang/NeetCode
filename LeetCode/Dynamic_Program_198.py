"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

"""

"""
The answer was provided by GPT4.
Could be found that the natural of dynamic programming is to use two swap two variables and use a temp variable to assist them.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Initialize two previously max values
        prev1, prev2 = 0, 0
        # Iterate over all the house
        for money in nums:
            # print(prev1, prev2, "money=", money, "temp=", max(prev1, prev2+money))

            # Calc the current max money by either robbing or skipping this house
            temp = max(prev1, prev2 + money)
            # Update prev2 and prev1 for the next iteration (to follow the constraint)
            prev2 = prev1
            prev1 = temp

        # As prev1=temp, after iterating through all houses, prev1 will hold the maximum amount of money you can rob.
        return prev1