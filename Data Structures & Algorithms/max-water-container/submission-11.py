class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_amount_of_water = 0
        while(i<j):
            amount_of_water = min(heights[i],heights[j])*(j-i)
            max_amount_of_water = max(amount_of_water,max_amount_of_water)
            if(heights[i]>heights[j]):
                j = j - 1
            else:
                i = i + 1
        return max_amount_of_water






        