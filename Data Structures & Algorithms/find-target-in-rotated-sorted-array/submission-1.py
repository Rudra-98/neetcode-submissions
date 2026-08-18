class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        m = len(nums) - 1
        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) ==1 and nums[0] != target:
            return -1
        while l <= m:
            mid = (l + m) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[len(nums) - 1] and target > nums[len(nums)-1]:
                m = mid -1
            elif nums[mid] >= nums[0] and target < nums[0]:
                l = mid +1
            elif  target >= nums[mid]:
                l = mid +1
            elif  target < nums[mid]:
                m = mid - 1

        return -1
        
        
        