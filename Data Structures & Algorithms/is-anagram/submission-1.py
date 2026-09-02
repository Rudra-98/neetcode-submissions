class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        str_1_frequency = {}
        str_2_frequency = {}
        
        for char in s:
            if char not in str_1_frequency:
                str_1_frequency[char] = 1
            else:
                str_1_frequency[char] += 1
        for char in t:
            if char not in str_2_frequency:
                str_2_frequency[char] = 1
            else:
                str_2_frequency[char] += 1
        
        for char in s:
            if char not in t:
                return False
            elif str_1_frequency[char] != str_2_frequency[char]:
                return False
            
        return True