class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        stats = {}
        maxlen = 0
        while r < len(s):
            s0 = s[r]
            gt = stats.get(s0, 0)
            stats[s0] = gt + 1
            maxchar = max(stats.values())
            sm = sum(stats.values())
            to_replace = sm - maxchar
            add = min(to_replace, k)
            print(stats)
            print(f"{add}:{maxchar}:{maxlen}:{to_replace}")
            if (r -l + 1) - maxchar > k:
                s1 = s[l]
                stats[s1] = stats[s1] - 1
                l = l + 1
            
            if maxchar + add > maxlen:
                maxlen = (r -l + 1)
            r = r + 1
        return maxlen            

             