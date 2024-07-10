"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.



Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # JUST: Imagine a wright list people=[2 3 4 5 7 8] with limit=8

        # Sort the people list first in ascending order
        people = sorted(people)

        # get the length of people list
        people_len = len(people)

        # Initialize the min-max pointers according to the value(weight)
        min_idx = 0
        max_idx = people_len - 1

        # Initialize the num of boats
        boat = 0

        # Iterate over the list
        while min_idx <= max_idx:
            max_w = people[max_idx]
            min_w = people[min_idx]
            # Case1: the boat can only take most weighted people at max_idx
            if (max_w == limit) or (max_w + min_w > limit):
                boat += 1
                # update the idx
                max_idx -= 1

            # Case2: the boat can take 2 people
            else:
                boat += 1
                # update the idx
                max_idx -= 1
                min_idx += 1

        return boat




