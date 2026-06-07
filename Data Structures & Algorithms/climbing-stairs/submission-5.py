class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * (n + 2)
        ways[n+1] = 0   
        i = n
        while(i >= 0):
            if i == n:
                ways[i] = 1
            else:
                ways[i] = ways[i+1] + ways[i+2]
            i=i-1
        return ways[0]

            
        