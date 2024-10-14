""""
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

"""
Should consider the center: odd center or even center, like "bb", "bcb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(set(s)) < 2:
            return s

        # Initialize the max palindromic substring
        max_sub = s[0]  # As the test case indecades inputting "ac" should return "a"

        # Iterate over entire string, the range ensure L and R valid
        for i in range(len(s)):
            # Initialize the current palindromic substring
            curr_sub = ""

            # Case1: To process the case like "bb"
            # get the two pointers L,R
            L = i - 1
            R = i + 1
            C = i  # center
            if L >= 0 and s[L] == s[C]:
                while L >= 0 and C < len(s):
                    if s[L] != s[C]:
                        break
                    curr_sub = s[L:C + 1]  # should plus 1 because if s="babad", then s[1:2] ="a"
                    L -= 1
                    C += 1
                # Comapre the max substring with the current substring
                if len(curr_sub) > len(max_sub):
                    max_sub = curr_sub

            # Case2: To process the case like "bcb"
            # get the two pointers L,R
            L = i - 1
            R = i + 1
            C = i  # center
            while L >= 0 and R < len(s):
                if s[L] != s[R]:
                    break
                curr_sub = s[L:R + 1]  # should plus 1 because if s="babad", then s[1:2]="a"
                L -= 1
                R += 1
            # Comapre the max substring with the current substring
            if len(curr_sub) > len(max_sub):
                max_sub = curr_sub

        return max_sub
