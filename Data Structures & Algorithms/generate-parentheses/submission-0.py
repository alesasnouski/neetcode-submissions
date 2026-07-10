class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def generate(m_open, m_cl, pref):
            if len(pref) < 2 * n:
                if m_open < n:
                    generate(m_open + 1, m_cl, f"{pref}(")
                if m_cl < n and m_open > m_cl:
                    generate(m_open, m_cl + 1, f"{pref})")
            else:
                result.append(pref)

        generate(0, 0, "")

        return result