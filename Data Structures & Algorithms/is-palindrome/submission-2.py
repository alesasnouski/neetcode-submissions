class Solution:
    def isPalindrome(self, s: str) -> bool:
        strng = ""
        for s0 in s:
            if s0.isalnum():
                strng = strng + s0.lower()
        is_palindrome = False

        str_m_len = 1 + len(strng) // 2 
        if len(strng) > 0:
            for i in range(str_m_len):
                j = -1 * i - 1
                if strng[i] == strng[j]:
                    is_palindrome = True
                else:
                    is_palindrome = False
                    break
        else:
            return True            

        return is_palindrome
