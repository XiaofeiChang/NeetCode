"""
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.



Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"


Constraints:

0 <= s.length <= 1000
t.length == s.length + 1
s and t consist of lowercase English letters.
"""


"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # find the difference by set
        diff = set(t) - set(s) # now diff is the type of Set()
        # convert diff to string
        result = "".join(diff)
        return result

        
        
# THIS METHOD ISN'T WORK AS THE ADDED LETTER MIGHT BE A DUPLICATED LETTER IN S

"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # find the difference by set
        diff = set(t) - set(s)  # now diff is the type of Set()
        # convert diff to string
        result = "".join(diff)

        # SO FAR
        # # THIS METHOD ISN'T WORK AS THE ADDED LETTER MIGHT BE A DUPLICATED LETTER IN S

        # SPECIAL CASE
        if result is "":
            # creat dict for t and s
            t_dict = {}
            for key in t:
                if key in t_dict:
                    # increment the value
                    t_dict[key] += 1
                else:
                    t_dict[key] = 1

            s_dict = {}
            for key in s:
                if key in s_dict:
                    # increment the value
                    s_dict[key] += 1
                else:
                    s_dict[key] = 1

            # compare the difference
            for key, _ in t_dict.items():
                # if the values are not equal, return our target output
                if t_dict[key] != s_dict[key]:
                    result = key

        return result
