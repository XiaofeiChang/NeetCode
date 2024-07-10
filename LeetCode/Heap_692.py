"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.



Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.


Constraints:

1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]


Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
"""

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # preprocessing
        # Sort the list by lexicographical order (ascending)
        words = sorted(words, key=str.lower)



        # Count the frequency efficiently (N.B. freq.type() is like Dictionary)
        freq = Counter(words)

        # Create a min-heap to keep track of the top k frequent words
        hp = []

        # append all the tuples and sort them by count using heap
        for word, count in freq.items():
            heapq.heappush(hp, (-count, word))# use negative to get the opposite of the nunmber, so that the max count be come the min count, which could use the min-heap as a max-heap



        # Create a list to save the result
        result = []
        # reteive the first k words
        for _ in range(k):
            # get the word from the tuple (-count, word)
            word = heapq.heappop(hp)[1]

            # append this word to the result list
            result.append(word)

        return result




