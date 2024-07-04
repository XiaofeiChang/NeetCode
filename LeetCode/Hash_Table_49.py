"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


# Main idea: use the sorted letter as key to group the original words as key-value pairs e.g. {"abt": ["bat"], "ant": ["nat","tan"], ...}
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dict
        my_dict = {}

        # iterate over the array
        for s in strs:
            # get the key-value pair
            value = s
            key = "".join(
                sorted(s))  # ''.join(sorted(my_string)): Joins the sorted list of characters back into a single string.

            # check if the key is already in the dict
            if key in my_dict:
                # append the new word
                (my_dict[key]).append(value)
            else:
                # create a new pair, following the format
                my_dict[key] = [value]

        # retrieve all the values to formalize the return format
        result = list(my_dict.values())
        return result

