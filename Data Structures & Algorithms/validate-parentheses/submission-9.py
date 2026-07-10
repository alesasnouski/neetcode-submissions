class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        st = list()
        for s0 in s:
            if s0 in "([{":
                st = [s0] + st
            elif len(st) > 0 and ((s0 == ")" and st[0] == "(") or (s0 == "]" and st[0] == "[") or (s0 == "}" and st[0] == "{")):
                st = st[1:]
            else:
                return False
        if len(st) == 0:
            return True        
        else:
            return False           
