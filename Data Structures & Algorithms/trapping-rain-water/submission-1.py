class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = height[0]
        maxr = height[len(height) - 1]
        l= 1
        r = len(height) - 2
        max_water  = 0
        while l<=r:
            if maxl<=maxr:
                water_stored = maxl - height[l]
                maxl = max(maxl, height[l])
                l = l + 1
            else:
                water_stored = maxr - height[r]
                maxr = max(maxr, height[r])
                r = r - 1
            if water_stored > 0:
                max_water = max_water + water_stored
        return max_water

        