class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        char_freq = {}
        k_found = False
        max_len = -float('inf')
        while j < len(s):
            if not k_found:
                if s[j] not in char_freq:
                    char_freq[s[j]]=1
                else:
                    char_freq[s[j]]+=1
            window = j - i + 1
            max_freq = max(char_freq.values())
            if window - max_freq > k:
                char_freq[s[i]] -= 1
                if char_freq[s[i]] == 0:
                    del char_freq[s[i]]
                i = i + 1
                k_found = True
            else:
                max_len = max(max_len, j - i + 1)
                j = j + 1
                k_found = False
        return max_len