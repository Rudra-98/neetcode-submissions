class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = []
        for num in nums:
            if num not in set_nums:
                set_nums.append(num)
            else:
                return True
        else:
            return False