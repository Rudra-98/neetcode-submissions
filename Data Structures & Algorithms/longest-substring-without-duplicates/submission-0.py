class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        d = {}
        max_string_len = 0
        while j < len(s):
            if s[j] not in d:
                d[s[j]] = 1
                string_len = j - i + 1
                j = j + 1
            else:
                d[s[i]] = d[s[i]] - 1
                if d[s[i]] == 0:
                    del d[s[i]]
                i = i + 1
            max_string_len = max(max_string_len, string_len)
        return max_string_len

 

            
        