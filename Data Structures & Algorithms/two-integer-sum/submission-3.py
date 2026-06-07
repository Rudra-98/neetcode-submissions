class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = list(nums)
        index = -1
        for i in range(0,len(nums)):
            find_value = target-nums[i]
            if  find_value in a:
                for j in range(0,len(a)):
                    if j!=i and a[j] == find_value:
                        index = j
                        break
                if index != -1:
                    break
        return [i,index]
                
        