class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_dict = {}
        freq_count = [[]] * (len(nums) + 1)
        end_result = []
        for item in nums:
            if item in freq_dict:
                freq_dict[item] = freq_dict[item] + 1
            else:
                freq_dict[item] = 1

        for key, value in freq_dict.items():
            if freq_count[value]:
                freq_count[value] = freq_count[value] + [key]
            else:
                freq_count[value] = [key]

        j = len(freq_count)-1
        while len(end_result) < k:
            if freq_count[j]:
                for ele in freq_count[j]:
                    end_result.append(ele)
            j = j - 1

        return end_result





        