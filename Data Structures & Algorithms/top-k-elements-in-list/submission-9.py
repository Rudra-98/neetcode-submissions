class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_1 = {}
        result = [[]] * (len(nums) + 1)
        final_result =[]
        for ele in nums:
            if ele in dict_1:
                dict_1[ele] = dict_1[ele] + 1
            else:
                dict_1[ele] = 1

        for key, value in dict_1.items():
            if result[value] != []:
                result[value].append(key)
            else:
                result[value]=[key]

        j = len(result)-1
        while(len(final_result) < k):
            if result[j]:
                for u in result[j]:
                    final_result.append(u)
            j = j-1
        return  final_result

        

        