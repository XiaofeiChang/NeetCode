"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


一般情况:把n级台阶时的跳法看成是n 的函数，记为f(n)。
当n>2 时，第一次跳的时候就有两种不同的选择:一是第一次只跳1 级，此时跳法数目等于后面剩下的n-1 级台阶的跳法数目，即为f(n-1);另外一种选择是第一次跳2 级，此时跳法数目等于后面剩下的n-2 级台阶的跳法数目，即为f(n-2)。
因此n 级台阶时的不同跳法的总数f(n)=f(n-1)+ f(n-2)。
"""



"""Solution 1: Time Exceed Limitation"""
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n==0 or n==1:
#             return 1

#         return self.climbStairs(n-1) + self.climbStairs(n-2)


"""Solution2: No recursion, only use two 'memory' (Dynamic Programming), avoiding time exceed error (See NeetCode)"""
class Solution:
    def climbStairs(self, n: int) -> int:
        # if n<2, directly return
        if n < 2:
            return n

        # Initialize the list
        dp = [0, 1]
        i = 2
        while i <= n + 1:
            temp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = temp
            i += 1

        return dp[1]



""""N.B.
The Question 509 is directly a fibonacci problem, where the only difference is "while i <= n + 1:" and "while i <= n"
Here is the explanation by GPT:

***
Climbing Stairs (while i <= n + 1):
The loop goes up to n + 1 because you're calculating the number of ways to reach the n-th step. The extra iteration accounts for calculating the last step (n), ensuring all possible ways are counted.

***
Fibonacci (while i <= n):
The loop stops at n because you're directly calculating the n-th Fibonacci number. No extra step is needed, so once you reach n, the calculation is complete.

In short, the climbing stairs problem involves calculating up to the n-th step, hence n + 1, while Fibonacci only needs to compute exactly F(n), so n is enough.



"""