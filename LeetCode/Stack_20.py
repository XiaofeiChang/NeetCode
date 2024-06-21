"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # avoid single char
        if len(s) <= 1:
            return False

        # replace all pairs of closed bracket with ''
        s = re.sub(r'\(\)', '', s)
        s = re.sub(r'\{\}', '', s)
        s = re.sub(r'\[\]', '', s)

        # if the s is still not empty, then return false
        if len(s) != 0:
            return False
        else:
            return True


