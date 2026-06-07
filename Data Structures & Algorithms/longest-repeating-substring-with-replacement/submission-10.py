class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        max_char_freq = 0
        ans = -1
        char_dict = {}
        while(j<len(s)):
            if s[j] in char_dict:
                char_dict[s[j]] = char_dict[s[j]] + 1
            else:
                char_dict[s[j]] = 1
            # get the maximum character frequency from the dict
            max_char_freq = max(char_dict.values())
            window = j - i + 1
            while(window - max_char_freq>k):
                char_dict[s[i]] = char_dict[s[i]] - 1
                i = i + 1
                max_char_freq = max(char_dict.values())
                window = j - i + 1

            j = j + 1
            ans = max(ans, window)
        
        return ans
        
        