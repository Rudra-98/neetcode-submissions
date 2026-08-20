class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq_dict = {}
        for i in range(0,len(nums)):
            if nums[i] in freq_dict:
                freq_dict[nums[i]] = freq_dict[nums[i]] + 1
            else:
                freq_dict[nums[i]] = 1
        for i in range(0,len(nums)):
            if freq_dict[nums[i]] > 1:
                return nums[i]


        