class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        aset = set(nums)
        max_seq = 1
        seq = 0
        if len(nums) in [0,1]:
            return len(nums)
        for num in aset:
            if num-1 not in aset:
                seq = seq+1
                num_1 = num+1
                while(num_1 in aset):
                        seq = seq+1
                        num_1 = num_1+1
                max_seq = max(seq,max_seq)
                seq = 0

        return max_seq
        
                
        


        


        
        
        