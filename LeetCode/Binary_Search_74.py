"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Two special cases
        min_num = matrix[0][0]
        max_num = matrix[-1][-1]
        if target < min_num or target > max_num:
            return False

        target_row = []
        # Focus on the row first
        for row in matrix:
            min_num = row[0]
            max_num = row[-1]
            if target >= min_num and target <= max_num:
                target_row = row
                break

        # Then find out if the target in target_row by two pointers
        L = 0
        R = len(target_row) - 1
        while L <= R: # If you don't make it equal, the test case with input matrix [[1]] will not pass
            mid = (L + R) // 2
            mid_val = target_row[mid]
            if mid_val == target:
                return True
                break
            elif mid_val < target:
                L = mid + 1
            elif mid_val > target:
                R = mid - 1

        return False