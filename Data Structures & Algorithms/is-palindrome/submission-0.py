import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        stre = re.sub(r"[^a-zA-Z0-9]","",s)
        st = stre.lower()
        if st[::-1] == st:
            return True
        return False
            