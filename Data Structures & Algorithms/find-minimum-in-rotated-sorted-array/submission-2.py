class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        m = len(nums) - 1
        if len(nums)==1:
            return nums[0]
        while l <= m:
            mid = (l + m) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid-1]:
                return nums[mid+1]
            elif mid == 0 or nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] <= nums[len(nums)-1]:
                m = mid-1
            elif nums[mid] >= nums[0]:
                l = mid + 1
        
        