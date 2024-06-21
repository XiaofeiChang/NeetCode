"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # get the lenght of num1 and nums2
        len1 = len(nums1)
        len2 = len(nums2)

        # initialize ans
        ans = []

        # iterate over nums1
        for i in range(0, len1):
            n1 = nums1[i]
            # find the index j such that n1 == nums1[i] == nums2[j]
            j0 = nums2.index(n1)

            # initialize the value of greater elem
            greater_elem = -1

            # determine the next greater element of nums2[j]
            for j in range(j0, len2):
                n2 = nums2[j]
                if n2 > n1:
                    greater_elem = n2
                    break

            # append the elem to ans
            ans.append(greater_elem)

        return ans

