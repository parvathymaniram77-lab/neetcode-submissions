class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for x in s:
            x = x.upper()
            if not  x.isalnum(): 
                continue
            t += x
        rev = t[::-1]
        if t != rev:
            return False
        return True

