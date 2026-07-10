class Solution:
    from collections import defaultdict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for strng in strs:
            strng1 = ''.join(sorted(strng))
            d[strng1].append(strng)
        return list(d.values())