class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * (n + 2)

        ways[n] = 1      # 1 way to be at the top
        ways[n+1] = 0    # beyond top is not a valid start

        for i in range(n-1, -1, -1):
            ways[i] = ways[i+1] + ways[i+2]

        return ways[0]

            
        