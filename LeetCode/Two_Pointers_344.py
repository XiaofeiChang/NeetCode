""""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character."""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # get the length of s
        s_len = len(s)
        # The rounding of mid index is to deal with the odd/even len of s
        mid_idx = round(s_len / 2)

        # initialize the L & R pointers
        L_idx = 0
        R_idx = s_len - 1

        # Iterate over the list and swap every pair of LR indexes
        for _ in range(mid_idx):
            # get the original values at the positions
            L_val = s[L_idx]
            R_val = s[R_idx]
            # Swap
            s[L_idx] = R_val
            s[R_idx] = L_val

            # Update two pointers
            L_idx += 1
            R_idx -= 1

