class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) > 0:
            substr_len = 1
        else:
            return 0    
        for (i, strng) in enumerate(s):
            local_buf = [strng]
            for n in s[i+1:]:
                if n not in local_buf:
                    local_buf.append(n)
                    if len(local_buf) > substr_len:
                        substr_len = len(local_buf)
                else:
                    break
        return substr_len                    


