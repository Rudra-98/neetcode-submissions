class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_water = -float('inf')
        while i < j:
            current_water = min(heights[i], heights[j])*(j-i)
            if heights[i] > heights[j]:
                j = j -1
            else:
                i = i + 1

            max_water = max(max_water, current_water)

        return max_water