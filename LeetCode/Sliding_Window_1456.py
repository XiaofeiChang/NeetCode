"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.



Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length

"""

"""



In this solution, the time complexity is much longer than the other one as there is a nested while loop within the for loop.




class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if s is None:
            return 0


        # As s consists of lowercase English letters, we initialize the set
        vowel_set = ['a', 'e', 'i', 'o','u']
        max_vowel = 0

        # It is known that the sliding window is in a fixed size, there fore we don't iterate over all the list
        max_L = len(s) - k
        for L in range(max_L+1):
            # The initialize the number of vowel in the current sliding window
            curr_vowel = 0
            R = L + k - 1
            sub_s = s[L:R+1]
            for c in sub_s:
                if c in vowel_set:
                    curr_vowel += 1
                    # if the number equals the max (k), directly return (early stop)
                if curr_vowel == k:
                    return k
            max_vowel = max(max_vowel, curr_vowel)

        return max_vowel
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if s is None:
            return 0

        # As s consists of lowercase English letters, we initialize the set
        vowel_set = ['a', 'e', 'i', 'o', 'u']
        max_vowel = 0

        # Case1: The initial window case:
        for L in range(0, k):
            if s[L] in vowel_set:
                max_vowel += 1

        # The num of vowel in the current sliding window
        curr_vowel = max_vowel

        # Case2: The onward cases:
        max_L = len(s) - k

        for L in range(1, max_L + 1):

            R = L + k - 1

            # Only consider the beginning and the ending of the curr substring, as the other elem overlap with the previous case
            if s[L - 1] in vowel_set:
                curr_vowel -= 1
            if s[R] in vowel_set:
                curr_vowel += 1

            max_vowel = max(max_vowel, curr_vowel)

            # if the number equals the max (k), directly return (early stop)
            if max_vowel == k:
                return k

        return max_vowel
