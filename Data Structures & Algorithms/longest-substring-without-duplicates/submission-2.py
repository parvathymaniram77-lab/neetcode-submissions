class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0
        curr_len = 0
        seen = set()
        while r <= len(s)-1: 
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                curr_len = r-l #refer notes
                max_len = max(curr_len,max_len)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
                r += 1
                curr_len = r-l #refer notes
                max_len = max(curr_len,max_len)
        return max_len

